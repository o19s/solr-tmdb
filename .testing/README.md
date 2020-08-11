## Testing TLRE examples

TLRE examples are vunerable to changes in external tooling (Splainer) and Solr itself. So to ensure things are ready to go for training we've scripted these "tests" to check all of the examples.

#### Splainer

These tests check that changes to Splainer don't damage TLRE examples.

Splainer links from the slides are stored in `splainer_links_solr.csv`. The script `splainer_puppet_solr.py` will visit each one of the links and report the HTTP status code back.

These tests assume you are running the local Solr TMDB setup.

Setup your virtual environment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run regression tests
```
python splainer_puppet_solr.py
```

This will record the status code in the CSV file and print the number of failed queries to console.

#### Newman

These tests check that version changes in Solr don't damage TLRE examples.

[Newman](https://github.com/postmanlabs/newman) is the command line tool for managing Postman collections. All examples from the class, beyond just the links to Splainer, are included in the collection `../solr_postman_collection.json`

```
newman run --global-var "solr_host=localhost:8983" ../solr_postman_collection.json
```
