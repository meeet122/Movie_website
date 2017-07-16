import webbrowser
class Movie():
      def __init__ (self, title, story_line, poster_url, trailer_url):
          self.movie_title = title
          self.movie_story_line = story_line
          self.movie_poster_url = poster_url
          self.movie_trailer_url = trailer_url

      def show_poster(self):
          webbrowser.open(self.movie_poster_url)
      def show_trailer(self):
          webbrowser.open(self.movie_trailer_url)
