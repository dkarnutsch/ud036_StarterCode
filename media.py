class Movie():
    """ Movie class holding all information about a movie """

    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer):
        """ Constructor for the movie class

        Args:
            movie_title: The title of the movie
            movie_storyline: short plot of the movie
            movie_poster: URL of the poster image (cover)
            movie_trailer: URL of the trailer (youtube)
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
