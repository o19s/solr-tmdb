import json


def rawTmdbMovies(tmdb_source_file):
    return json.load(open(tmdb_source_file))


def writeTmdbMovies(rawMoviesJson, path):
    with open(path, 'w') as f:
        json.dump(rawMoviesJson, f)

def tmdbMovies(tmdb_source_file):
    tmdbMovies = rawTmdbMovies(tmdb_source_file)
    for movieId, tmdbMovie in tmdbMovies.items():
        yield (movieId, tmdbMovie)
