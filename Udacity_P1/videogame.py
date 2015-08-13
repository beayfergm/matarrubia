from mediaitem import MediaItem;

class Videogame(MediaItem):
	''' 
	Declares a Videogame object which inherits from MediaItem
	In addition to the MediaItem class members, every videogame has:
	studio_name: name of the studio which built the game
	pegi_rating: PEGI rating for the item
	'''

	PEGI_RATINGS = ["P3", "P7", "P12", "P16", "P18"];

	def __init__(self, title, thumbnail_url, preview_youtube_url, studio_name, pegi_rating_index):
		MediaItem.__init__(self, title, thumbnail_url, preview_youtube_url);
		self.studio_name = studio_name;
		self.pegi_rating = Videogame.PEGI_RATINGS[pegi_rating_index];