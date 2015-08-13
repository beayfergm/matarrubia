import webbrowser;

class MediaItem():
	'''
	Declares a MediaItem object. 
	Every MediaItem is defined by:
	title: Media Item Title
	thumbnail_url: link to an image representing the MediaItem
	preview_youtube_url: link to a youtube video representing the MediaItem
	'''
	def __init__(self, title, thumbnail_url, preview_youtube_url):
		self.title = title;
		self.thumbnail_url = thumbnail_url;
		self.preview_youtube_url = preview_youtube_url;

	def open_url(self, url):
		# Opens the url in a separate webbrowser tab
		webbrowser.open(url);