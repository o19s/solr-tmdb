import requests
import json

class SolrColl:
    def __init__(self, solrColl='http://localhost:8983/solr/tmdb/', verbose=True):
        self.solrColl = solrColl
        if self.solrColl[-1] != '/':
            self.solrColl += '/'
        self.verbose = verbose

    def ifVerbosePrint(self, aStr):
        if self.verbose:
            print(aStr)


    def query(self, handler, params):
        queryUrl = self.solrColl + handler
        self.ifVerbosePrint("GET %s" % queryUrl)
        self.ifVerbosePrint(json.dumps(params, indent=2))
        resp = requests.get(queryUrl, params=params)
        self.ifVerbosePrint(resp.status_code)
        if resp.status_code < 200 or resp.status_code >= 300:
            print(resp.text)
            raise IOError("Solr Error %s" % resp.text)
        return json.loads(resp.text)


    def reloadFeatures(self, features):
        url = self.solrColl + "schema/feature-store"
        deletePath = url + '/_DEFAULT_'
        self.ifVerbosePrint("DELETE %s" % url)
        resp = requests.delete(deletePath)
        self.ifVerbosePrint(resp.status_code)
        featureSet = [feature for _, feature in features]
        self.ifVerbosePrint("POST %s" % url)
        self.ifVerbosePrint(json.dumps(featureSet, indent=2))
        resp = requests.post(url, json.dumps(featureSet))
        self.ifVerbosePrint(resp.status_code)
        if resp.status_code < 200 or resp.status_code >= 300:
            print(resp.text)
            raise IOError("Solr Error %s" % resp.text)



