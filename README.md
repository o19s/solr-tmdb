Solr Index for the [The Movie Database](http://themoviedb.com).

# Run Solr index

If you have _Docker_ you can run:
```
docker run -it -p 8983:8983 -v $PWD/solr_home:/opt/mysolrhome -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr
```

Otherwise:

1. Download and unpack [Solr 7.4.0](http://archive.apache.org/dist/lucene/solr/7.4.0/solr-7.4.0.zip)
2. Run Solr pointing at the Solr Home directory included here

```
./bin/solr start -f -s /path/to/solr-tmdb/solr_home/
```

In your browser, navigate to "http://localhost:8983/solr/" to confirm Solr is running

# Index TMDB movies

1. Install [Python 3.6](https://www.python.org/downloads/) and the [pysolr library](https://github.com/django-haystack/pysolr) library
2. Run `python indexTmdb.py` to index movies

# Confirm Solr has TMDB movies

Navigate [here](http://localhost:8983/solr/tmdb/select?q=title:lego) and confirm you get results.
