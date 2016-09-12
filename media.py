import webbrowser


class Video():
    """ This class provides a way to store video parent related information """

    def __init__(self, title, rating, duration):
        self.title = title
        self.rating = rating
        self.duration = duration

    def show_info(self):
        print("Title - "+self.title)
        print("Duration - "+self.duration)


class Movie(Video):
    """ This class provides a way to store movie related information """

    def __init__(self, title, rating, duration, movie_storyline, poster_image,
                 trailer_youtube,  *args, **kwargs):
        Video.__init__(self, title, rating, duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)



