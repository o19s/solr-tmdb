#!/usr/bin/env bash

if [ "$(uname -s)" == 'Linux' ]; then
   # necessary on Linux according to https://github.com/docker-solr/docker-solr/blob/master/README.md
   # docker does volume mount as solr user, which has usually no permissions on the host system
   sudo chown -R 8983:8983 solr_home   
fi

docker run -p 8983:8983 -v "${PWD}/solr_home:/opt/mysolrhome" -e SOLR_HOME=/opt/mysolrhome -e INIT_SOLR_HOME=yes solr:8.4.1
