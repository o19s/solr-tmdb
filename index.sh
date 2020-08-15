#!/bin/bash

curl 'http://localhost:8983/solr/tmdb/update?commit=true' --data-binary @tmdb_solr.json -H 'Content-type:application/json'
