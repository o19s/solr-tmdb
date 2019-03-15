Solr Index for the [The Movie Database](http://themoviedb.com).

This repository is part of the _Think Like a Relevancy Engineer_ training provided by [OpenSource Connections](https://opensourceconnections.com/events/training/).

# Run Solr index

1. Download and unpack [Solr 7.4.0](http://archive.apache.org/dist/lucene/solr/7.4.0/solr-7.4.0.zip)
2. Run Solr pointing at the Solr Home directory included here

```
./bin/solr start -f -s /path/to/solr-tmdb/solr_home/
```

In your browser, navigate to "http://localhost:8983/solr/" to confirm Solr is running

# Index TMDB movies

1. Download [tmdb.json](http://es-learn-to-rank.labs.o19s.com/tmdb.json)
2. Install [Python 3.6](https://www.python.org/downloads/) and the [pysolr library](https://github.com/django-haystack/pysolr) library
3. Run `python indexTmdb.py` to index movies

# Confirm Solr has TMDB movies

Navigate [here](http://localhost:8983/solr/tmdb/select?q=title:lego) and confirm you get results.
