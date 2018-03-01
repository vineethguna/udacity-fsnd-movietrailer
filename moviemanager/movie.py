# Movie class is a class representation of a single movie. It contains title, box art url, trailer link
class Movie(object):
    def __init__(self, title, box_art_url, trailer_link):
        self._title = title
        self._box_art_url = box_art_url
        self._trailer_link = trailer_link

    def get_title(self):
        return self._title

    def get_box_art_url(self):
        return self._box_art_url

    def get_trailer_link(self):
        return self._trailer_link
