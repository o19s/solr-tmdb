

if __name__ == "__main__":
    import pysolr
    solr = pysolr.Solr('http://localhost:8983/solr/tmdb', timeout=100)
    solr.delete(q='*:*', commit=True)