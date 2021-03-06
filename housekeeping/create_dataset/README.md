# Generating the TMDB dataset

Periodically we update the TMDB dataset as new movies come out, or new data sources are added.

1. Get the latest TMDB dump using the https://github.com/o19s/tmdb_dump project.

2. Create the Solr schema formatted JSON file:

Pass in the TMDB extract file and the name of the resulting Solr JSON file.

```
python3 createSolrTmdbDataset.py tmdb_2020-08-10.json tmdb_solr.json
```

3. Zip and store the file in the root directory

```
zip tmdb_solr.json.zip tmdb_solr.json
cp tmdb_solr.json ../../
```

4. Don't forget to check the new zip file in!


https://raw.githubusercontent.com/o19s/tmdb_dump/master/tmdb_dataflows.png

# Understanding Data Structure

You can use `jq` to parse the JSON.   Just unzip a chunk and then do:

> cat tmdb_solr_2020-08-11.json | jq .

Or, to look at a specific movie dataset, look it up by id:

> jq '.[] | select(.id=="87381")' tmdb_solr_2020-08-11.json
