from mediaitem import MediaItem;


class Videogame(MediaItem):
	
	''' 
	Declares a Videogame object which inherits from MediaItem
	In addition to the MediaItem class members, every videogame has:
	studio_name: name of the studio which built the game
	pegi_rating: PEGI rating for the item
	'''

	PEGI_RATINGS = {
	3: "http://www.pegi.info/en/index/id/33/media/img/320.gif", 
	7: "http://www.pegi.info/en/index/id/33/media/img/321.gif", 
	12: "http://www.pegi.info/en/index/id/33/media/img/322.gif", 
	16: "http://www.pegi.info/en/index/id/33/media/img/323.gif", 
	18: "http://www.pegi.info/en/index/id/33/media/img/324.gif"
	};

	def __init__(self, title, thumbnail_url, preview_youtube_url, studio_name, pegi_rating):
		MediaItem.__init__(self, title, thumbnail_url, preview_youtube_url);
		self.studio_name = studio_name;

		if(pegi_rating in Videogame.PEGI_RATINGS):
			self.pegi_rating_img_url = Videogame.PEGI_RATINGS[pegi_rating];
		else:
			# Default PEGI is 3
			self.pegi_rating_img_url = Videogame.PEGI_RATINGS[3];