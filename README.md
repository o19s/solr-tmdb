Solr Index for the [The Movie Database](http://themoviedb.com).

This repository is part of the _Think Like a Relevancy Engineer_ training provided by [OpenSource Connections](https://opensourceconnections.com/events/training/).

# What you'll get out of it

* How to measure search quality
* Removing the fear from relevance experimentation
* Becoming 'hypothesis driven' in relevance work
* Elasticsearch relevance tuning techniques
* Building semantic search
* Implementing machine learning to improve relevance (ie Learning to Rank)
* Access to the best experts in the world on Elasticsearch relevance for brainstorming your problems

### Day One - Managing, Measuring, and Testing Search Relevance

This day helps the class understand how working on relevance requires different thinking than other engineering problems. We teach you to measure search quality, take a hypothesis-driven approach to search projects, and safely 'fail fast' towards ever improving business KPIs

* What is search?
* Holding search accountable to the business
* Search quality feedback
* Hypothesis-driven relevance tuning
* User studies for search quality
* Using analytics & clicks to understand search quality

### Day Two - Engineering Relevance with Elasticsearch|Solr

This day demonstrates relevance tuning techniques that actually work. Relevance can't be achieved by just tweaking field weights: Boosting strategies, synonyms, and semantic search are discussed. The day is closed introducing machine learning for search (aka "Learning to Rank").

* Getting a feel for Elasticsearch|Solr
* Signal Modeling (data modeling for relevance)
* Dealing with multiple, competing objectives in search relevance
* Synonym strategies that actually work
* Taxonomy-based Semantic Search
* Introduction to Learning to Rank

_You'll also receive a copy of [Relevant Search](https://www.manning.com/books/relevant-search) written by OpenSource Connections CTO Doug Turnbull and OpenSource Connections Alum John Berryman_

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
