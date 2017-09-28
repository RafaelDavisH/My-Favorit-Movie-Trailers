import fresh_tomatoes
import media

# Bourne Indentity: movie title, storyline, poster image and movie trailer
the_bourne_identity = media.Movie(
    "The Bourne Identity", """An amnesiac attempting to discover
    his true identity amidist a clandestine conspiracy within
    the Central Intelligence Agency.""",
    "https://vignette2.wikia.nocookie.net/bourne/images/d/d0/Identity_poster_01.jpg/revision/latest?cb=20120223045603",
    "https://youtu.be/cD-uQreIwEk"
    )



# Italian Job: movie title, storyline, poster image and movie trailer
the_italian_job = media.Movie(
    "The Italian Job",
    """Is about a team of thieves who plan to steal gold grom a former
    associate who double-crossed them.""",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Italianjob.jpg",
    "https://www.youtube.com/watch?v=5Eyw-Qiwpj0"
    )

# Chronicles of Narnia: movie title, storyline, poster imag and movie trailer
the_chronicles_of_narnia = media.Movie(
    "The Voyage of the Dawn Treader",
    "Three Narnian years after the events of Prince Caspian.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/The_Voyage_of_the_Dawn_Treader_poster.jpg",
    "https://www.youtube.com/watch?v=OubkxGzVuxU")

# Saving Private Ryan: movie title, storyline, poster imag and movie trailer
saving_private_ryan = media.Movie(
    "Saving Private Ryan",
    """A 1998 American epic war drama film set during the Invasion
    of Normandy in World War II.""",
    "https://upload.wikimedia.org/wikipedia/en/a/ac/Saving_Private_Ryan_poster.jpg",
    "https://www.youtube.com/watch?v=RYExstiQlLc"
    )

# Secret Life of Walter Mitty: movie title, storyline, poster imag and movie trailer
the_secret_life_of_walter_mitty = media.Movie(
    "The Secret Life of Walter Mitty",
    """Walter Mitty is a negative assest manager at Life magazine
    who daydreams of adventures.""",
    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg",
    "https://www.youtube.com/watch?v=eoILTydXrTY"
    )

# Dark Knight Rises: movie title, storyline, poster imag and movie trailer
the_dark_knight_rises = media.Movie(
    "The Dark Knight Rises",
    """Eight years after the events of The Dark Knight, merciless
    revolutionary Bane forces an older Bruce Wayne to resume his
    role as Batman and save Gotham City from nuclear destruction.""",
    "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
    "https://www.youtube.com/watch?v=ay-Xg1oTeAs"
    )

# Set movies to pass to the media file
movies = [the_bourne_identity,
          the_italian_job,
          the_chronicles_of_narnia,
          saving_private_ryan,
          the_secret_life_of_walter_mitty,
          the_dark_knight_rises
          ]

# Open HTML file in webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
