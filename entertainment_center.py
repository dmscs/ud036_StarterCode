import media
import fresh_tomatoes


# list of movies
pixar_movies = [
	{
	'title': 'Toy Story', 
	'poster_image_url': 'https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg',
	'trailer_youtube_url': 'https://youtu.be/KYz2wyBy3kc'
	},
	{
	'title': 'Up', 
	'poster_image_url': 'http://vignette3.wikia.nocookie.net/pixar/images/d/de/Up_ver4_xlg.jpg/revision/latest?cb=20110414093901',
	'trailer_youtube_url': 'https://youtu.be/pkqzFUhGPJg'
	}
]


# make list of movies using movie class
def get_movie_list(favorite_movies):
	movies = []
	
	for movie in pixar_movies:
		movies.append(media.Movie(movie['title'], movie['poster_image_url'], movie['trailer_youtube_url']))

	return movies



if __name__ == '__main__':
	# make movie list
	movies = get_movie_list(pixar_movies)

	# creates webpage with movies and trailers
	fresh_tomatoes.open_movies_page(movies)