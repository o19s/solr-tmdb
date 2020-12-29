#!/bin/bash

# delete (or wipe) the tmdb index and reindex
curl http://localhost:8983/solr/tmdb/update --data '<delete><query>*:*</query></delete>' -H 'Content-type:text/xml; charset=utf-8'

curl http://localhost:8983/solr/tmdb/update --data '<commit/>' -H 'Content-type:text/xml; charset=utf-8'

curl 'http://localhost:8983/solr/tmdb/update?commit=true' --data-binary @tmdb_solr.json -H 'Content-type:application/json'
