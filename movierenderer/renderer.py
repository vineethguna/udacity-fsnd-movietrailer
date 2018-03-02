import webbrowser
import os
import re


class Renderer(object):
    HTML_HEAD_CONTENT_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'html', 'head.html')
    HTML_BODY_CONTENT_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'html', 'content.html')
    HTML_TILE_CONTENT_FILE = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'html', 'movietile.html')

    def __init__(self, movies):
        """
        Creates a HTML renderer which can render the movie trailer website
        using the list of movies stored by movie manager
        :param movies: List of movies
        """
        self._movies = movies
        self._head_content = open(Renderer.HTML_HEAD_CONTENT_FILE, 'r').read()
        self._body_content = open(Renderer.HTML_BODY_CONTENT_FILE, 'r').read()
        self._movie_tile_content = \
            open(Renderer.HTML_TILE_CONTENT_FILE, 'r').read()

    def launch_website(self):
        """
        Renders the html content and launches the movie trailer
        website in your default browser
        :return: None
        """
        output_html = open(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'html', 'fresh_tomatoes.html'), 'w')
        rendered_html = self._render_website()
        output_html.write(rendered_html)
        output_html.close()

        # open the output file in the browser
        url = os.path.abspath(output_html.name)
        # open in a new tab, if possible
        webbrowser.open('file://' + url, new=2)

    def _render_website(self):
        """
        Renders the html content and return the html content
        :return: str
        """
        movie_tile_content = self._render_movie_tiles_content()
        body_content = self._render_body_content(movie_tile_content)
        return self._head_content + body_content

    def _render_movie_tiles_content(self):
        """
        Renders the tile content for each movie
        :return: str
        """
        content = ''
        for movie in self._movies:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(r'(?<=v=)[^&#]+',
                                         movie.get_trailer_link())
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.get_trailer_link())
            trailer_youtube_id = youtube_id_match.group(0) \
                if youtube_id_match else None

            # Append the tile for the movie with its content filled in
            content += self._movie_tile_content.format(
                movie_title=movie.get_title(),
                poster_image_url=movie.get_box_art_url(),
                trailer_youtube_id=trailer_youtube_id
            )
        return content

    def _render_body_content(self, tile_content):
        """
        Takes movie tile content as argument and
        renders the actual html body content
        :param tile_content: tile content of all the movies
        :return: str
        """
        return self._body_content.format(movie_tiles=tile_content)
