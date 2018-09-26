import pysolr


def indexableMovies(tmdbJson):
    """ Generates TMDB movies, similar to how ES Bulk indexing
        uses a generator to generate bulk index/update actions """
    from tmdbMovies import tmdbMovies
    for movieId, tmdbMovie in tmdbMovies(tmdbJson):
        print("Indexing %s" % movieId)
        try:
            releaseDate = None
            if 'release_date' in tmdbMovie and len(tmdbMovie['release_date']) > 0:
                releaseDate = tmdbMovie['release_date'] + 'T00:00:00Z'

            yield {'id': movieId,
                   'title': tmdbMovie['title'],
                   'overview': tmdbMovie['overview'],
                   'tagline': tmdbMovie['tagline'],
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
    tmdbJson = 'tmdb.json'
    solrUrl = 'http://localhost:8983/solr/tmdb'
    if len(argv) > 1:
        tmdbJson = argv[1]
        solrUrl = argv[2]
    solr = pysolr.Solr(solrUrl, timeout=100)
    solr.add(indexableMovies(tmdbJson))
