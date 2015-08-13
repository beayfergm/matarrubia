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
	18
	);

jet_force_gemini = videogame.Videogame(
	"Jet Force Gemini", 
	"http://www.dpaddbags.com/blog/wp-content/uploads/2013/02/jfg.jpg", 
	"https://www.youtube.com/watch?v=nLT46BqE-OI",
	"Rare",
	12
	);

interstellar = movie.Movie(
	"Interstellar", 
	"https://d3ui957tjb5bqd.cloudfront.net/uploads/2014/11/interstellar-poster-3.png", 
	"https://www.youtube.com/watch?v=0vxOhd4qlnA",
	"Matthew McConaughey, Anne Hathaway, Jessica Chastain",
	"November 7th, 2014",
	"http://www.imdb.com/title/tt0816692/"
	);

fftactics = videogame.Videogame(
	"Final Fantasy Tactics", 
	"http://img3.wikia.nocookie.net/__cb20080914034013/finalfantasy/images/b/b6/Fftnacover.jpg", 
	"https://www.youtube.com/watch?v=feP9LG_VgHc",
	"Square Enix",
	7
	);

efalcatraz = movie.Movie(
	"Escape From Alcatraz", 
	"http://images.moviepostershop.com/escape-from-alcatraz-movie-poster-1979-1020466272.jpg", 
	"https://www.youtube.com/watch?v=UT4kc5jG990",
	"Clint Eastwood, Patrick McGoohan, Roberts Blossom",
	"December 19th, 1979",
	"http://www.imdb.com/title/tt0079116/"
	);

# Adding all items to a list
media_items = [];
media_items.append(reservoir_dogs);
media_items.append(diablo_two);
media_items.append(jet_force_gemini);
media_items.append(interstellar);
media_items.append(fftactics);
media_items.append(efalcatraz);

# Creates an html page with all the information and opens it
fresh_tomatoes.open_movies_page(media_items);