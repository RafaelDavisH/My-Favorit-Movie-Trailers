#!/usr/bin/env python2.7

import fresh_tomatoes
import media


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
    "https://goo.gl/PMzJ1P",
    "https://www.youtube.com/watch?v=OubkxGzVuxU")

# Saving Private Ryan: movie title, storyline, poster imag and movie trailer
saving_private_ryan = media.Movie(
    "Saving Private Ryan",
    """A 1998 American epic war drama film set during the Invasion
    of Normandy in World War II.""",
    "https://goo.gl/QSjRQo",
    "https://www.youtube.com/watch?v=RYExstiQlLc"
    )

# The Bourne Indentity: movie title, storyline, poster image and movie trailer
the_bourne_identity = media.Movie(
    "The Bourne Identity", """An amnesiac attempting to discover
    his true identity amidist a clandestine conspiracy within
    the Central Intelligence Agency.""",
    "https://goo.gl/Zdbhw4",
    "https://youtu.be/cD-uQreIwEk"
    )

# The Bourne Supremacy: movie title, storyline, poster image and movie trailer
the_bourne_supremacy = media.Movie(
    "The Bourne Supremacy",
    """Jason focuses in learning more of his past as he is
    once more enveloped in a conspiracy invoving the CIA and Operation
    Treadstone.""",
    "https://goo.gl/uJaHHr",
    "https://youtu.be/Y-HqyyfBbSo"
  )

# The Bourne Ultimatum: movie title, storyline, poster image and movie trailer
the_bourne_ultimatum = media.Movie(
    "The Bourne Ultimatum",
    """Jason continues his search for information about his past before he was
    part of Operation Treadstone and becomes a target of a similar assassin
    program. """,
    "https://goo.gl/W1Ue6C",
    "https://youtu.be/ZT2ZxjUjSo0"
)

# The Bourne legacy: movie title, storyline, poster image and movie trailer
the_bourne_legacy = media.Movie(
    "The Bourne Legacy",
    """In The Bourne Legacy, Aaron Cross is a member of a black ops program
    called Operation Outcome whose subjects are genetically enhanced. He must
    run for his life.""",
    "https://goo.gl/6okU8T",
    "https://youtu.be/cdtUdEoE-Q4"
)

# Jason Bourne: movie title, storyline, poster image and movie trailer
jason_bourne = media.Movie(
    "Jason Bourne",
    """Bourne remains on the run from CIA hit squads as he tries to uncover
    hidden truths about his father. CIA director Robert Dewey orders the CIA
    head of cyber-security Heather Lee to hunt him down.""",
    "https://goo.gl/ZBDFr2",
    "https://youtu.be/v71ce1Dqqns"
)

# Dark Knight Rises: movie title, storyline, poster imag and movie trailer
the_dark_knight_rises = media.Movie(
    "The Dark Knight Rises",
    """Eight years after the events of The Dark Knight, merciless
    revolutionary Bane forces an older Bruce Wayne to resume his
    role as Batman and save Gotham City from nuclear destruction.""",
    "https://goo.gl/fwGxHX",
    "https://www.youtube.com/watch?v=ay-Xg1oTeAs"
    )

# Jurassic Park: movie title, storyline, poster image and movie trailer
jurassic_park = media.Movie(
    "Jurassic Park",
    """Industrialist John Hammond and his bioengineering company, InGen, have
    created a theme park called Jurassic Park on Isla Nublar, a Costa Rican
    Island, pupulated with cloned dinosaurs.""",
    "https://goo.gl/jyE4mL",
    "https://youtu.be/QWBKEmWWL38"
)

# The Lost World: movie title, storyline, postyer image and movie trailer
the_lost_world = media.Movie(
    "The Lost World",
    """Four years after the events of the Jurassic Park dinosaurs roaming free
    in the Isla Nublar. An expedition its set to stop of the capturing of the
    dinosaurs.""",
    "https://goo.gl/yDsNqa",
    "https://youtu.be/RxrvaneULkE"
    )

# Secret Life of Walter Mitty: movie title, storyline, poster imag and movie
# trailer
the_secret_life_of_walter_mitty = media.Movie(
    "The Secret Life of Walter Mitty",
    """Walter Mitty is a negative assest manager at Life magazine
    who daydreams of adventures.""",
    "https://goo.gl/MiWNye",
    "https://www.youtube.com/watch?v=eoILTydXrTY"
    )

# Set movies to pass to the media file
movies = [the_italian_job,
          the_chronicles_of_narnia,
          saving_private_ryan,
          the_bourne_identity,
          the_bourne_supremacy,
          the_bourne_ultimatum,
          the_bourne_legacy,
          the_dark_knight_rises,
          jason_bourne,
          jurassic_park,
          the_lost_world,
          the_secret_life_of_walter_mitty,
          ]

# Open HTML file in webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
