import fresh_tomatoes
import media

# Instances of class movie

underworld = media.Movie("Underworld",  # Movie Title
                         "(R)",  # Movie Rating
                         "121 min",  # Movie Length
                         "https://en.wikipedia.org/wiki/Underworld_%282003_"
                         "film%29",  # Movie Infomation
                         "http://ia.media-imdb.com/images/M/MV5BMjIxNDExNDE"
                         "yMV5BMl5BanBnXkFtZTcwODY1OTkxMw@@._V1_SY317_C"
                         "R0,0,214,317_AL_.jpg",  # Poster Site
                         "https://www.youtube.com/watch?v=MqT-e44kIM8&oref="
                         "https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DMq"
                         "T-e44kIM8&has_verified=1")  # Video Site

avatar = media.Movie("Avatar",  # Movie Title
                     "(PG-13)",  # Movie Rating
                     "162 min",  # Movie Length
                     "https://en.wikipedia.org/wiki/Avatar_%282009_film%29",
                     # Movie Infomation
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5"
                     "BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,"
                     "214,317_AL_.jpg",  # Poster Site
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY"
                     # Video Site)

the_bourne_identity = media.Movie("The Bourne Identity",  # Movie Title
                                  "(PG-13)",  # Movie Rating
                                  "119 min",  # Movie Length
                                  "https://en.wikipedia.org/wiki/The_Bourne_"
                                  "Identity_%282002_film%29",
                                  # Movie Infomation
                                  "http://ia.media-imdb.com/images/M/MV5BMTQ"
                                  "3MDA4MDIyN15BMl5BanBnXkFtZTYwOTg0N"
                                  "jk4._V1_SX214_AL_.jpg",  # Poster Site
                                  "https://www.youtube.com/watch?v=FpKaB5dvQ4"
                                  "g"  # Video Site)

the_dark_knight_rises = media.Movie("The Dark Knight Rises",  # Movie Title
                                    "(PG-13)",  # Movie Rating
                                    "164 min",  # Movie Length
                                    "https://en.wikipedia.org/wiki/The_Dark_"
                                    "Knight_Rises",  # Movie Infomation
                                    "http://pre07.deviantart.net/83dc/th/pre"
                                    "/f/2012/005/7/a/the_dark_knight_rises_"
                                    "poster_iii_by_mike1306-d4lf9xi.jpg",
                                    # Poster Site
                                    "https://www.youtube.com/watch?v=GokKUq"
                                    "LcvD8"  # Video Site)

the_devil_wears_prada = media.Movie("The Devil Wears Prada",  # Movie Title
                                    "(PG-13)",  # Movie Rating
                                    "109 min",  # Movie Length
                                    "https://en.wikipedia.org/wiki/The_Devil_"
                                    "Wears_Prada_%28film%29",
                                    # Movie Infomation
                                    "https://trinemalde.files.wordpress.com/"
                                    "2014/07/the_devil_wears_prada_"
                                    "poster.jpg?w=460&h=649", # Poster Site
                                    "https://www.youtube.com/watch?v=XTDSwAxl"
                                    "Nhc"  # Video Site)

begin_again = media.Movie("Begin Again",  # Movie Title
                          "(R)",  # Movie Rating
                          "104 min",  # Movie Length
                          "https://en.wikipedia.org/wiki/Begin_Again_%28"
                          "film%29",  # Movie Infomation
                          "http://www.impawards.com/2014/posters/begin_again"
                          ".jpg",  # Poster Site
                          "https://www.youtube.com/watch?v=uTRCxOE7Xzc"
                          # Video Site)

# Append each movie to a list
movies = [underworld, avatar, the_bourne_identity, the_dark_knight_rises,
          the_devil_wears_prada, begin_again]
# Call open_movies
fresh_tomatoes.open_movies_page(movies)

