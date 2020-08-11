import json


def rawTmdbMovies():
    return json.load(open('tmdb.json'))


def writeTmdmMovies(rawMoviesJson, path):
    with open(path, 'w') as f:
        json.dump(rawMoviesJson, f)

def tmdbMovies():
    tmdbMovies = rawTmdbMovies()
    for movieId, tmdbMovie in tmdbMovies.items():
        yield (movieId, tmdbMovie)
