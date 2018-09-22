import json
from solr import SolrColl
import atexit
from loadFeatures import featureOrdToName

def featureCsvToList(features, ftrMapping):

    ftrNameToOrd = {name: _ord for (_ord, name) in ftrMapping}
    ftrDict = dict(feature.split("=") for feature in features.split(","))

    rVal = [0.0] * len(ftrMapping)

    for ftrName, value in ftrDict.items():
        _ord = ftrNameToOrd[ftrName]
        rVal[_ord - 1] = value

    return rVal


def logFeatures(solrColl, judgmentsByQid):
    idx = 0

    ftrMapping = featureOrdToName()

    featuresPerDoc = {}

    for qid, judgments in judgmentsByQid.items():
        keywords = judgments[0].keywords
        docIds = [judgment.docId for judgment in judgments]
        idsQuery = 'id:(' + ' '.join(docIds) + ')'

        resp = solrColl.query(handler='select', params={'q': idsQuery,
                                                        'rows': '100',
                                                        'fl': "id,title,[features efi.keywords='%s']" % keywords} )



        for doc in resp['response']['docs']:
            docId = doc['id']
            features = doc['[features]']
            featuresPerDoc[docId] = featureCsvToList(features, ftrMapping)

        print("REBUILDING TRAINING DATA for %s (%s/%s)" % (judgments[0].keywords, idx, len(judgmentsByQid)))
        # Append features from ES back to ranklib judgment list
        for judgment in judgments:
            try:
                features = featuresPerDoc[judgment.docId] # If KeyError, then we have a judgment but no movie in index
                judgment.features = features
            except KeyError:
                print("Missing movie %s" % judgment.docId)
        idx += 1




def buildFeaturesJudgmentsFile(judgmentsWithFeatures, filename):
    with open(filename, 'w') as judgmentFile:
        for qid, judgmentList in judgmentsWithFeatures.items():
            for judgment in judgmentList:
                judgmentFile.write(judgment.toRanklibFormat() + "\n")


if __name__ == "__main__":
    from judgments import judgmentsFromFile, judgmentsByQid

    solrColl = SolrColl('http://localhost:8983/solr/tmdb/')
    judgmentsByQid = judgmentsByQid(judgmentsFromFile('movie_judgments.txt'))
    logFeatures(solrColl, judgmentsByQid)
    buildFeaturesJudgmentsFile(judgmentsByQid, "sample_judgments_wfeatures.txt")

