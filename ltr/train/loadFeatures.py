import json

def getFeature(ftrId):
    return json.loads(open('%s.json' % ftrId).read())


def featureOrdToName():
    features = []
    for ftrId, feature in eachFeature():
        features.append((ftrId, feature['name']))
    return features

def eachFeature():
    try:
        ftrId = 1
        while True:
            parsedJson = getFeature(ftrId)
            yield ftrId, parsedJson
            ftrId += 1
    except IOError:
        pass



if __name__ == "__main__":
    from solr import SolrColl
    solrHost='http://localhost:8983'
    solrColl = SolrColl('http://localhost:8983/solr/tmdb/')
    solrColl.reloadFeatures(features=eachFeature())
    print(featureOrdToName())
