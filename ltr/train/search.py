baseQuery = {
    "size": 5,
    "query": {
        "match": {
            "text_all.en": ""
        }
    },
    "rescore": {
        "window_size": 1000,
        "query": {
            "rescore_query": {

                "sltr": {
                    "params": {
                        "keywords": "",
                        "expansions": ""
                    },
                    "model": "",
              }
            }

        }
   }
}

def ltrQuery(keywords, modelName):
    import json
    from expansions import expansionTextAllBigrams, expansionTextAll, expansionGenre
    #baseQuery['query']['sltr']['params']['expansions_text_all_bigrams'] = expansionTextAllBigrams(es, keywords)
    #baseQuery['query']['sltr']['params']['expansions_text_all'] = expansionTextAll(es, keywords)
    #baseQuery['query']['sltr']['params']['expansions_genre'] = expansionGenre(es, keywords)
    baseQuery['query']['match']['text_all.en'] = keywords
    baseQuery['rescore']['query']['rescore_query']['sltr']['params']['keywords'] = keywords
    baseQuery['rescore']['query']['rescore_query']['sltr']['model'] = model
    print("%s" % json.dumps(baseQuery))
    return baseQuery


if __name__ == "__main__":
    import configparser
    from sys import argv
    from elasticsearch import Elasticsearch

    config = configparser.ConfigParser()
    config.read('settings.cfg')
    esUrl=config['DEFAULT']['ESHost']

    es = Elasticsearch(esUrl, timeout=1000)
    model = "test_6"
    if len(argv) > 2:
        model = argv[2]
    keywords = argv[1]
    results = es.search(index='tmdb', doc_type='movie', body=ltrQuery(keywords, model))
    for result in results['hits']['hits']:
             print("%s " % (result['_source']['title']))
             print("%s " % (result['_score']))
             print("%s " % (result['_source']['vote_average']))
             print("%s " % (result['_source']['vote_count']))
             print("%s " % (result['_source']['overview']))
             print("---------------------------------------")

