#!/bin/bash

echo 'Wait for solr to be responsive'
./wait-for-solr.sh 10 5

echo "Going to load data into Solr"


echo "Running indexMlTmdb.py"
python3 /train/indexTmdb.py /train/tmdb.json http://solr:8983/solr/tmdb


echo "Done with setup"
