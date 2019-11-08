Solr Index for the [The Movie Database](http://themoviedb.com).

This repository is part of the _Think Like a Relevancy Engineer_ training provided by [OpenSource Connections](https://opensourceconnections.com/events/training/).

The code in this repo requires [Python 3](https://www.python.org/downloads/). So if you have both Python 2 and Python 3 installed, you may need to append the version number to your `python` commands or set up an appropriate virtual environment.

```
 python3 indexTmdb.py
```

# Clone this repo

```
git clone https://github.com/o19s/solr-tmdb.git
```

After you clone this repo, change into the newly created directory.

# Run Solr index

Two options exist to run Solr.

### Docker option

If you have [Docker](https://www.docker.com/products/docker-desktop) installed and running.

```
docker run -p 8983:8983 -v $PWD/solr_home:/opt/mysolrhome -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr:7.7.1
```

### Local option

1. Download and unpack [Solr 7.4.0](http://archive.apache.org/dist/lucene/solr/7.4.0/solr-7.4.0.zip)

2. Run Solr pointing at the Solr Home directory included here

```
./bin/solr start -f -s /path/to/solr-tmdb/solr_home/
```

Regardless of the option you choose, navigate to [http://localhost:8983/solr/](http://localhost:8983/solr/) to confirm Solr is running.

# Index TMDB movies

1. Download [tmdb.json](http://es-learn-to-rank.labs.o19s.com/tmdb.json)

```
curl -o tmdb.json http://es-learn-to-rank.labs.o19s.com/tmdb.json
```

2. Install the [pysolr](https://github.com/django-haystack/pysolr) library

Optional: set up a virtual environment.

```
python -m venv .
source bin/activate 
```

Required:

```
pip install pysolr
# or
pip install -r requirements.txt
```

3. Index movies

```
python indexTmdb.py
```

# Confirm Solr has TMDB movies

Navigate [here](http://localhost:8983/solr/tmdb/select?q=title:lego) and confirm you get results.
