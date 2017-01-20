import pysolr


def tmdbMovies():
    """ Generates TMDB movies, similar to how ES Bulk indexing
        uses a generator to generate bulk index/update actions """
    import json
    tmdbMovies = json.loads(open('tmdb.json').read())
    for movieId, tmdbMovie in tmdbMovies.items():
        print("Indexing %s" % movieId)
        try:
            yield {'id': movieId,
                   'title': tmdbMovie['title'],
                   'overview': tmdbMovie['overview'],
                   'tagline': tmdbMovie['tagline'],
                   'directors': [director['name'] for director in tmdbMovie['directors']],
                   'cast': [castMember['name'] for castMember in tmdbMovie['cast']],
                   'genres': [genre['name'] for genre in tmdbMovie['genres']]}
        except KeyError as k: # Ignore any movies missing these attributes
            print(k)
            continue


if __name__ == "__main__":
    solr = pysolr.Solr('http://localhost:8983/solr/tmdb', timeout=100)
    solr.add(tmdbMovies())
