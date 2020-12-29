# Powershell script for Windows 10 and above to index the TMDB JSON file.

# delete (or wipe) the tmdb index and reindex
Invoke-WebRequest -Method POST -Uri 'http://localhost:8983/solr/tmdb/update' -Body '<delete><query>*:*</query></delete>' -Content-type 'text/xml; charset=utf-8'

Invoke-WebRequest -Method POST -Uri 'http://localhost:8983/solr/tmdb/update' -Body '<commit/>' -ContentType 'text/xml; charset=utf-8'


$data = Get-Content 'tmdb_solr_file.json'
Invoke-WebRequest -Method POST -Uri 'http://localhost:8983/solr/tmdb/update' -ContentType 'application/json' -UseBasicParsing -Body $data
