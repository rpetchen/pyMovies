import movies
import fresh_tomatoes
# create 6 instances of movies using the movies.Movie constructor
# Godzilla moive: movie title, storyline, poster image, trailer
Godzilla = movies.Movie("Godzilla",
                         "The 1954 original!!",
                         "https://upload.wikimedia.org/wikipedia/commons/0/01/Gojira_1954_poster_3.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=1csyf1OzKlc")
# Godzilla Raids Again: movie title, storyline, poster image, trailer
Godzilla_Raids = movies.Movie("Godzilla Raids Again",
                             "GIGANTS THE FIRE MONSTER",
                             "https://upload.wikimedia.org/wikipedia/commons/2/27/Gojira_no_gyakushu_poster_2.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=VOo0CstvnM4")
# Godzilla vs King Kong: movie title, storyline, poster image, trailer
Godzilla_Kong = movies.Movie("Godzilla vs Kong",
                             "Kong Vs Godzilla!!",
                             "http://1125996089.rsc.cdn77.org/wp-content/uploads/2015/11/king-kong-vs-godzilla-1.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=sGYl-93cBBA")
# Godzilla vs Mothra: movie title, storyline, poster image, trailer
Godzilla_Moth = movies.Movie("Godzilla vs Mothra",
                            "Mothra Vs Godzilla!!",
                            "http://www.angelfire.com/movies/8mmboxes/imagesscifi/godzvsthing.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=4bhoWfC1L9k")
# Ghidorah the three headed monster: movie title, storyline, poster image, trailer  # NOQA
Ghidorah = movies.Movie("Ghidorah, the Three-Headed Monster",
                        "Ghidora!!!!",
                        "https://i.ytimg.com/vi/VYX9mwsXM_M/maxresdefault.jpg",
                        "https://www.youtube.com/watch?v=vC4rMWD7MXw")
# Godzilla vs Monster Zero: movie title, storyline, poster image, trailer
Godzilla_zero = movies.Movie("Godzilla vs Monster Zero",
                             "Ghidorah Godzilla!!",
                             "https://i.pinimg.com/736x/0a/c2/3f/0ac23f6fdc8979da31749c6fdfad60a9--godzilla-vs-monster-movie.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=wjKgnHPnIJ0")
# list of the movie objects to pass to the open_movies_page function
movies = [Godzilla, Godzilla_Raids, Godzilla_Kong,
          Godzilla_Moth, Ghidorah, Godzilla_zero]

fresh_tomatoes.open_movies_page(movies)
