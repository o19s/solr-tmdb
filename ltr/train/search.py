from solr import SolrColl

def search(solrConn, model, keywords, rerankWeight):
    resp = solrConn.query(handler="select",
                            params={"q": keywords,
                                    "defType": "edismax",
                                    "qf": "text_all",
                                    "rq": "{!ltr model='%s' efi.keywords='%s' rerankDocs=100, rerankWeight=%s}" % (model, keywords, rerankWeight)})
    return resp




if __name__ == "__main__":
    import configparser
    from sys import argv

    config = configparser.ConfigParser()
    config.read('settings.cfg')
    solrColl=config['DEFAULT']['SolrColl']

    solrColl = SolrColl(solrColl=solrColl)
    model = "doug_6"
    resp = search(solrColl, model=model, keywords=argv[1], rerankWeight=1)
    for doc in resp['response']['docs']:
        print(doc['title'])
