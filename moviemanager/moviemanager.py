from .movie import Movie
import os
import pickle


# Movie Manager class handles addition of movies, storing the data offline, loading the movies data when launched again
class MovieManager(object):
    FILE_NAME_TO_PERSIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'movies.db')

    def __init__(self):
        self._movies = list()
        self._load_all_movies_from_file()

    def _load_all_movies_from_file(self):
        if os.path.isfile(MovieManager.FILE_NAME_TO_PERSIST):
            with open(MovieManager.FILE_NAME_TO_PERSIST, 'rb') as fd:
                while True:
                    try:
                        self._movies.append(pickle.load(fd))
                    except EOFError:
                        break

    def create_movie(self, title, box_art_url, trailer_url):
        new_movie = Movie(title, box_art_url, trailer_url)
        if self._movie_already_exists(new_movie):
            raise Exception("Movie already exists")
        self._store_movie(new_movie)

    def _store_movie(self, new_movie):
        self._movies.append(new_movie)
        with open(MovieManager.FILE_NAME_TO_PERSIST, 'ab') as fd:
            pickle.dump(new_movie, fd)

    def _movie_already_exists(self, new_movie):
        exists = False
        for movie in self.get_all_movies():
            if movie.get_title() == new_movie.get_title():
                exists = True
                break
        return exists

    def get_movie_with_title(self, title):
        for movie in self.get_all_movies():
            if movie.get_title == title:
                return movie

    def get_all_movies(self):
        return self._movies
