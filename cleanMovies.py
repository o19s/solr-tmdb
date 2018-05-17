
from tmdbMovies import rawTmdbMovies, writeTmdbMovies

def cleanTmdb():
    # Some movies are innapropriatte for delivering training
    # So we clean them up
    moviesJson = rawTmdbMovies()

