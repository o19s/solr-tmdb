# Generating the TMDB dataset

Periodically we update the TMDB dataset as new movies come out, or new data sources are added.

1. Get the latest TMDB dump from https://github.com/o19s/tmdb_dump.

2. Set up a virtual environment.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Create File

```
python3 createSolrTmdbDataset.py
```

4. Move the file up to the main /


https://raw.githubusercontent.com/o19s/tmdb_dump/master/tmdb_dataflows.png
