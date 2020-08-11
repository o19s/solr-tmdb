# Generating the TMDB dataset

Periodically we update the TMDB dataset as new movies come out, or new data sources are added.

1. Get the latest TMDB dump using the https://github.com/o19s/tmdb_dump project.

2. Set up a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Create the Solr schema formatted JSON file:

Pass in the TMDB extract file and the name of the resulting Solr JSON file.

```
python3 createSolrTmdbDataset.py tmdb_2020-08-10.json tmdb_solr_2020-08-11.json
```

4. Zip and store the file in the root directory


https://raw.githubusercontent.com/o19s/tmdb_dump/master/tmdb_dataflows.png
