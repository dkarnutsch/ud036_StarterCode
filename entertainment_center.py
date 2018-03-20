import fresh_tomatoes
import media

# Create movie instances
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

inception = media.Movie("Inception",
                        """A thief, who steals corporate secrets through the
                        use of dream-sharing technology.""",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=JEv8W3pWqH0")

fight_club = media.Movie("Fight Club",
                         "Rule 1: Don't talk about the Fight Club",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=G7tr7xcUCFA")

interstellar = media.Movie("Interstellar",
                           """A group of astronauts travel through a wormhole
                           in search of a new home for humanity""",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

butterfly_effect = media.Movie("Butterfly Effect",
                               """Evan Treborn suffers blackouts during
                               significant events of his life.""",
                               "https://upload.wikimedia.org/wikipedia/en/4/43/Butterflyeffect_poster.jpg",
                               "https://www.youtube.com/watch?v=B8_dgqfPXFg")

# Put movie instances in a list
movies = [toy_story, avatar, inception, fight_club, interstellar,
          butterfly_effect]

# Display movies page
fresh_tomatoes.open_movies_page(movies)
