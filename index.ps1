# Powershell script for Windows 10 and above to index the TMDB JSON file.

$data = Get-Content 'tmdb_solr_file.json'
Invoke-WebRequest -Method POST -Uri 'http://localhost:8983/solr/tmdb/update' -ContentType 'application/json' -UseBasicParsing -Body $data
