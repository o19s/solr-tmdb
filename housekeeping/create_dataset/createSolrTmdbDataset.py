from tmdbMovies import tmdbMovies
from tmdbMovies import writeTmdbMovies

def indexableMovies(tmdb_source_file):
    """ Generates TMDB movies, similar to how ES Bulk indexing
        uses a generator to generate bulk index/update actions """

    for movieId, tmdbMovie in tmdbMovies(tmdb_source_file):
        print("Indexing %s" % movieId)
        try:
            releaseDate = None
            if 'release_date' in tmdbMovie and len(tmdbMovie['release_date']) > 0:
                releaseDate = tmdbMovie['release_date'] + 'T00:00:00Z'

            yield {'id': movieId,
                   'title': tmdbMovie['title'],
                   'overview': tmdbMovie['overview'],
                   'tagline': tmdbMovie['tagline'],
                   'cast_nomv': " ".join([castMember['name'] for castMember in tmdbMovie['cast']]),
                   'directors': [director['name'] for director in tmdbMovie['directors']],
                   'cast': [castMember['name'] for castMember in tmdbMovie['cast']],
                   'genres': [genre['name'] for genre in tmdbMovie['genres']],
                   'release_date': releaseDate,
                   'vote_average': tmdbMovie['vote_average'] if 'vote_average' in tmdbMovie else None,
                   'vote_count': int(tmdbMovie['vote_count']) if 'vote_count' in tmdbMovie else None,
                   }
        except KeyError as k: # Ignore any movies missing these attributes
            print(k)
            continue


if __name__ == "__main__":
    from sys import argv

    tmdb_source_file = argv[1]
    tmdb_solr_file = argv[2]
    writeTmdbMovies(list(indexableMovies(tmdb_source_file=tmdb_source_file)),tmdb_solr_file)
