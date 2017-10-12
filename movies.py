import webbrowser


# Movie class used to create an instance of a movie with a title, storlyine, poster, and trailer # NOQA
class Movie():
    def __init__(self, movie_title, movie_storyline,
    	         poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
#movie method used to open up the youtube url in a browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)