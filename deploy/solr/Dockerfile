FROM solr:7.4.0

# Add customizations

USER root
COPY ./solr_home /solr_home
RUN chown -R 8983:8983 /opt/solr/server/solr
RUN chown -R 8983:8983 /solr_home
USER solr
