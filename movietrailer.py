from moviemanager.moviemanager import MovieManager
from movierenderer.renderer import Renderer
import argparse


# Movie manager object which acts as a simple database to store all movies
movie_manager = MovieManager()


def execute_add_command(args, parser):
    """
    Handles the "add" command of the command line tool
    It calls the create_movie method of movie manager
    to add movie data
    :param args: arguments passed to the add command
    :param parser: the argument parser object being used
    :return: None
    """
    if not args.title:
        parser.error("Title not specified")
    elif not args.art_url:
        parser.error("Box art url not specified")
    elif not args.trailer_url:
        parser.error("Trailer url not specified")
    movie_manager.create_movie(args.title, args.art_url, args.trailer_url)


def execute_launch_command(args, parser):
    """
    Handles the "launch" command of the command line tool
    It calls the launch_website method of Renderer which
    launches the website
    :param args: arguments passed to the launch command
    :param parser: the argument parser object being used
    :return: None
    """
    renderer = Renderer(movie_manager.get_all_movies())
    renderer.launch_website()


def main():
    """
    Starting point of this command line tool.
    :return: None
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='sub_command')

    add_parser = subparsers.add_parser('add', help='add --help')
    add_parser.add_argument('-t', '--title', dest='title',
                            help='Title of the movie')
    add_parser.add_argument('-i', '--art-url', dest='art_url',
                            help='Box art url of the movie')
    add_parser.add_argument('-y', '--trailer-url', dest='trailer_url',
                            help='Youtube trailer url of the movie')

    subparsers.add_parser('launch', help='add --help')

    args = parser.parse_args()
    if args.sub_command == 'add':
        execute_add_command(args, parser)
    elif args.sub_command == 'launch':
        execute_launch_command(args, parser)


if __name__ == '__main__':
    main()
