Solr Index for the [The Movie Database](http://themoviedb.com).

This repository is part of the _Think Like a Relevancy Engineer_ training provided by [OpenSource Connections](https://opensourceconnections.com/events/training/).

## Steps to get up and running:
- Download this repo
- Install Solr search engine and configuration (using either Docker or installing manually)
- Index the TMDB movie data
- Confirm Solr has the data
- Install Postman (optional)

# Download this repo

Download the zip from https://github.com/o19s/solr-tmdb/archive/master.zip, and
you will get the file `solr-tmdb-master.zip`.  Unzip this file, resulting in the
directory `solr-tmdb-master`.


After you have this download, change into the newly created directory.

# Install Solr

Two options exist to run Solr locally, however if neither of them will work for you, we do
have a public version of this dataset deployed at http://quepid-solr.dev.o19s.com:8985/solr/ that
you can use during the class as well, so don't fret if your environment won't let you set up Solr!

### Docker option (recommended)

If you have [Docker](https://www.docker.com/products/docker-desktop) installed and running.

Linux:
> ./docker.sh

Windows:
> powershell docker.ps1


### Local option

1. Download and unpack [Solr 8.11.1](https://archive.apache.org/dist/lucene/solr/8.11.1/solr-8.11.1.tgz)

2. Navigate into the newly unzipped directory.

3. Run Solr pointing at the TMDB Solr Home directory included in this repo.

Linux:
>bin/solr start -f -s /path/to/solr-tmdb-master/solr_home/

Windows 10:
>bin\solr start -f -s \path\to\solr-tmdb-master\solr_home\


Regardless of the option you choose, navigate to [http://localhost:8983/solr/](http://localhost:8983/solr/) to confirm Solr is running.

# Index TMDB movies

Unzip the `tmdb_solr.json.zip` file first.

```
unzip tmdb_solr.json.zip
```

Then send the unzipped `tmdb_solr.json` into Solr.

Linux:
> ./index.sh

Windows 10:
> powershell index.ps1

_If you get a permissions error, just open the index.ps1 file and copy and paste the contents into your Powershell console_

You are indexing a *big 100 mb file*, so this will take up to five minutes!

# Confirm Solr has TMDB movies

Navigate [here](http://localhost:8983/solr/tmdb/select?q=title:lego) and confirm you get results.

If you don't see any results, trigger a [manual commit](http://localhost:8983/solr/tmdb/update?commit=true).


# Postman

[Postman](https://www.postman.com/) is an API development tool, that helps build, run and manage API requests. The examples from the TLRE slides exist here too as a Postman Collection (`solr-postman_collection.json`). We like using Postman because it makes tinkering with query parameters nicer and we think it is a useful way to follow along as you learn about tuning search relevance.

If you want to use Postman during the TLRE class:

1. Download [Postman](https://www.postman.com/downloads/) for your OS
2. Open Postman and Import (top-menu >> File) `solr-postman-collection.json`
3. Define a global variable (grey eye icon in the upper-right) `solr_host` to point to your running Solr instance (default is `localhost:8983`)
4. Tinker with the base URL, Params or JSON Body (optional)
5. Press 'Send' (blue rectangle button right of URL bar)
