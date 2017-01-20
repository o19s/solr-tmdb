#!/bin/bash
set -x
# create solrcloud with colname $1

ZK_CONF_NAME="$1_conf"
SOLR_SRC=/home/doug/ws/lucene_solr_6_2_0

#/usr/local/solr-5.4.1/server/scripts/cloud-scripts/zkcli.sh -zkhost localhost:9983 -cmd upconfig -confdir /usr/local/solr-5.4.1/server/solr/configsets/basic_configs/conf -confname basic_configs 2>/var/log/zookeeper-config    .log

$SOLR_SRC/solr/server/scripts/cloud-scripts/zkcli.sh  -zkhost localhost:9983 -cmd upconfig -confdir $1/conf -confname $ZK_CONF_NAME

if [ "$2" = "CREATE" ]
then
    # create solrcloud coll
    curl "http://localhost:8983/solr/admin/collections?action=CREATE&collection.configName=$ZK_CONF_NAME&name=$1&numShards=1&replicationFactor=1&maxShardsPerNode=2"
elif [ "$2" = "DELETE" ]
then
    # Uploat the $1 conf dir here
    curl "http://localhost:8983/solr/admin/collections?action=DELETE&name=$1"
elif [ "$2" = "RELOAD" ]
then
    curl "http://localhost:8983/solr/admin/collections?action=RELOAD&collection.configName=$ZK_CONF_NAME&name=$1"
else
    echo "No action specified"
fi
