from mediaitem import MediaItem;

class Movie(MediaItem):
	''' 
	Declares a Movie object which inherits from MediaItem
	In addition to the MediaItem class members, every movie has:
	actors: main characters in the movie
	release_date: date when the movie was released
	imdb_url: url to the IMDB page for the film
	'''
	def __init__(self, title, thumbnail_url, preview_youtube_url, actors, release_date, imdb_url):
		MediaItem.__init__(self, title, thumbnail_url, preview_youtube_url);
		self.actors = actors;
		self.release_date = release_date;
		self.imdb_url = imdb_url;

	def open_imdb_page(self):
		# Opens the imdb page for this movie in a separate webbrowser tab
		open_url(self.imdb_url);
