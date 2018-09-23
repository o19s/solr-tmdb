# Learning to Rank Demo

This demo uses data from [TheMovieDB](http://themoviedb.org) (TMDB) to demonstrate using [Ranklib](https://sourceforge.net/p/lemur/wiki/RankLib/) learning to rank models with Solr.

# Install Dependencies and prep data...

This demo requires

- Python 3+
- Python `requests` libraries

## Download the TMDB Data & Ranklib Jar

The first time you run this demo, fetch RankyMcRankFace.jar (used to train model) and tmdb.json (the dataset used)

```
cd train
python prepare.py
```

## Start Solr/install plugin

Start a supported version of Solr and follow the [instructions to setup Solr LTR](https://lucene.apache.org/solr/guide/7_4/learning-to-rank.html), or use the config provided in this repo.

## Index to Elasticsearch

This script (in the parent directory) will index into the tmdb collection. 

```
cd ../..
python indexTmdb.py
```

# Onto the machine learning...

## TLDR

If you're actually going to build a learning to rank system, read past this section. But to sum up, the full Movie demo can be run by

```
cd ltr/train/
python train.py
```

Then you can search using

```
python search.py Rambo
```

and search results can be printed to the console.
