import movie
import videogame
import fresh_tomatoes

reservoir_dogs = movie.Movie(
	"Reservoir Dogs", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A",
	"Harvey Keitel, Tim Roth, Michael Madsen",
	"September 2nd, 1992",
	"http://www.imdb.com/title/tt0105236/"
	);

diablo_two = videogame.Videogame(
	"Diablo", 
	"https://upload.wikimedia.org/wikipedia/en/3/3a/Diablo_Coverart.png", 
	"https://www.youtube.com/watch?v=Fl5I5CUTqh4",
	"Blizzard Entertainment",
	4
	);

jet_force_gemini = videogame.Videogame(
	"Jet Force Gemini", 
	"http://www.dpaddbags.com/blog/wp-content/uploads/2013/02/jfg.jpg", 
	"https://www.youtube.com/watch?v=nLT46BqE-OI",
	"Rare",
	2
	);

interstellar = movie.Movie(
	"Interstellar", 
	"http://www.joblo.com/posters/images/full/interstellar-poster-2.jpg", 
	"https://www.youtube.com/watch?v=0vxOhd4qlnA",
	"Matthew McConaughey, Anne Hathaway, Jessica Chastain",
	"November 7th, 2014",
	"http://www.imdb.com/title/tt0816692/"
	);


media_items = [];
media_items.append(reservoir_dogs);
media_items.append(diablo_two);
media_items.append(jet_force_gemini);
media_items.append(interstellar);

fresh_tomatoes.open_movies_page(media_items);