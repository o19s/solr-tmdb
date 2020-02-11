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
<<<<<<< HEAD
docker pull solr:8.1
docker run -p 8983:8983 -v $(PWD)/solr_home:/opt/mysolrhome -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr:8.1
=======
docker pull solr:8.4.1
docker run -p 8983:8983 -v $(PWD)/solr_home:/opt/mysolrhome -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr:8.4.1
>>>>>>> update to Solr v8.4.1
```

### Local option

<<<<<<< HEAD
1. Download and unpack [Solr 8.1](http://http://archive.apache.org/dist/lucene/solr/8.1.1/8.1.1.zip)
=======
1. Download and unpack [Solr 8.4.1](http://mirror.metrocast.net/apache/lucene/solr/8.4.1/solr-8.4.1.zip)
>>>>>>> update to Solr v8.4.1

2. Navigate into the newly unzipped directory.

3. Run Solr pointing at the Solr Home directory included in this repo.

```
bin/solr start -f -s /path/to/solr-tmdb/solr_home/
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

If you don't see any results, trigger a [manuel commit](localhost:8983/solr/tmdb/update?commit=true).

# Postman

[Postman](https://www.postman.com/) is an API development tool, that helps build, run and manage API requests. The examples from the TLRE slides exist here too as a Postman Collection (`solr-TLRE-postman_collection.json`). We like using Postman becasue it makes tinkering with query parameters nicer and we think it is a useful way to follow along as you learn about tuning search relevance.

If you want to use Postman during the TLRE class:

1. Download [Postman](https://www.postman.com/downloads/) for your OS
2. Open Postman and Import (top-menu >> File) `solr-TLRE-postman_collection.json`
3. Define a global variable (grey eye icon in the upper-right) `solr-host` to point to your running Elasticsearch instance (default is `localhost:8983`)
4. Tinker with the base URL, Params or JSON Body (optional)
5. Press 'Send' (blue rectangle button right of URL bar)

This collection is also valuable for testing examples against new versions of Elasticsearch. Using Postman's command line tool [Newman](https://github.com/postmanlabs/newman) you can check all of the requests in the collection:

```
newman run --global-var "es_host=localhost:9200" es-TLRE-postman_collection.json
```
