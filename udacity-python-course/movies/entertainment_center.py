import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

wreck_it_ralph = media.Movie("Wreck It Ralph", "An arcarde villain dreams of becoming the hero", "https://upload.wikimedia.org/wikipedia/en/1/15/Wreckitralphposter.jpeg", "https://www.youtube.com/watch?v=87E6N7ToCxs")

movies = [toy_story, avatar, wreck_it_ralph]
fresh_tomatoes.open_movies_page(movies)
