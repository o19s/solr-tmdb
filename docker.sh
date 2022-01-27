#!/usr/bin/env bash
sudo chown -R 8983:8983 solr_home   # necessary on Linux, not Mac according to https://github.com/docker-solr/docker-solr/blob/master/README.md
docker run -p 8983:8983 -v $(PWD)/solr_home:/opt/mysolrhome -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr:8.4.1
