import json


def rawTmdbMovies(tmdbJson):
    return json.load(open(tmdbJson))


def writeTmdmMovies(rawMoviesJson, path):
    with open(path, 'w') as f:
        json.dump(rawMoviesJson, f)

def tmdbMovies(tmdbMovies):
    tmdbMovies = rawTmdbMovies(tmdbMovies)
    for movieId, tmdbMovie in tmdbMovies.items():
        yield (movieId, tmdbMovie)
