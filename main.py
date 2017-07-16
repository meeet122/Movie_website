import fresh_tomatoes
import webbrowser
import media

Tubelight = media.Movie("Tubelight",
                        "A war time drama film",
                        "https://en.wikipedia.org/wiki/File:Tubelight_Poster.jpg",
                        "https://www.youtube.com/watch?v=PGQRNKHJwH4")

#Tubelight.show_trailer()
#Tubelight.show_poster()
movies = [Tubelight]
fresh_tomatoes.open_movies_page(movies)

