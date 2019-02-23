# module provides interface to display web-based documents
import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    # This is how each instance is created
    # Each instance takes in a movie's: title, storyline, poster and trailer
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        # sets the title to match the movie's title
        self.title = movie_title
        # sets the storyline to match the movie's storyline
        self.storyline = movie_storyline
        # sets the poster url to match the movie's poster url
        self.poster_image_url = poster_image
        # sets the trailer url to match the movie's trailer url
        self.trailer_youtube_url = trailer_youtube

    # Opens youtube trailer in browser using webbrowser module
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

