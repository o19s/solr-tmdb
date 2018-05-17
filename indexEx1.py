import pysolr


def nameDocs():
    """ Generates TMDB movies, similar to how ES Bulk indexing
        uses a generator to generate bulk index/update actions """
    yield {
        'id': 1,
        'text': """What is the land speed of Luke sky walker dined with darth vader.
                   Darth vader is his father. Darth and Anakin
                   Skywalker. Luke's mom Padme Amidala was sad she couldn't make it. """
    }

    yield {
        'id': 2,
        'text': """Where is the land speed of  Bob's Big Boy is fantastic! I went there
                     with my son, Luke. He got a Luke Skywalker action figure! """
    }



if __name__ == "__main__":
    solr = pysolr.Solr('http://localhost:8983/solr/tmdb', timeout=100)
    solr.delete(q="*:*")
    solr.add(nameDocs())
