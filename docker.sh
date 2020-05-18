#!/bin/bash

docker run -p 8983:8983 -v $(PWD)/solr_home:/opt/mysolrhome -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr:8.4.1
