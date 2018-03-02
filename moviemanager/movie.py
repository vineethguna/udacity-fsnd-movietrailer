class Movie(object):
    def __init__(self, title, box_art_url, trailer_link):
        """
        Creates a Movie object which represents a single movie
        :param title: Title of the movie
        :param box_art_url: Box art url of the movie
        :param trailer_link: Youtube trailer link of the movie
        """
        self._title = title
        self._box_art_url = box_art_url
        self._trailer_link = trailer_link

    def get_title(self):
        """
        Returns the title of the movie
        :return: str
        """
        return self._title

    def get_box_art_url(self):
        """
        Returns the box art url of the movie
        :return: str
        """
        return self._box_art_url

    def get_trailer_link(self):
        """
        Return youtube trailer link of the movie
        :return: str
        """
        return self._trailer_link
