import movie
import fresh_tomatoes

reservoir = movie.Movie(
	"Reservoir Dogs", 
	"Crazy!", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A"
	);

reservoir2 = movie.Movie(
	"Reservoir Dogs", 
	"Crazy!", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A"
	);

reservoir3 = movie.Movie(
	"Reservoir Dogs", 
	"Crazy!", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A"
	);

reservoir4 = movie.Movie(
	"Reservoir Dogs", 
	"Crazy!", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A"
	);

reservoir5 = movie.Movie(
	"Reservoir Dogs", 
	"Crazy!", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A"
	);

reservoir6 = movie.Movie(
	"Reservoir Dogs", 
	"Crazy!", 
	"http://www.goldposter.com/wp-content/uploads/2015/04/Reservoir-Dogs_poster_goldposter_com_31.jpg", 
	"https://www.youtube.com/watch?v=vayksn4Y93A"
	);

movies = [];
movies.append(reservoir);
movies.append(reservoir2);
movies.append(reservoir3);
movies.append(reservoir4);
movies.append(reservoir5);
movies.append(reservoir6);

fresh_tomatoes.open_movies_page(movies);