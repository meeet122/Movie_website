import fresh_tomatoes
import webbrowser


Tubelight = media.Movie("Tubelight",
                        "A war time drama film",
                        "https://en.wikipedia.org/wiki/File:Tubelight_Poster.jpg",
                        "https://www.youtube.com/watch?v=PGQRNKHJwH4")
movies = [Tubelight]
fresh_tomatoes.open_movies_page(movies)

