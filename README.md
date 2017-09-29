# My Favorite Movie Trailers

A simple and dynamic project website that showcase a few of my favorite movie trailers. There are layout in a responsive grid.

**Each movie has:**

- Poster image
- Title
- Storyline
- Trailer youtube video.

**You'll be running `entertainment_center.py` script to load the website, but first:**


### You'll Need:

`fresh_tomatoes.py`

`media.py`

`entertainment_center.py`


### Fresh Tomatoes

The `fresh_tomatoes.py` has `open_movies_page()` function that will
take in the list of movies and generate an HTML file including its content,
producing a website to showcase my favorite movie trailers.


### Media

You will find inside `media.py` a class called `Movie()`, which contains the
`__init__` constructor, four instance variables and an instance method.

*`__int__` constructor*

This constructor has five arguments, including `self`, which are:

1. `self`

2. `movie_title`

3. `movie_storyline`

4. `poster_image`

5. `trailer_youtube`


*Instance Variables:*

1. `title`

2. `stotyline`

3. `poster_image_url`

4. `trailer_youtube_url`


*Instance Method*

`show_trailer()` is the method that will show the movie youtube trailer in a
new tab. The method initiates `webbrowser.open(self.trailer_youtube_url)`.


### Entertainment Center

`entertainment_center.py` contains the instances of `Movie()`. The movie
objects calls the constructor `media.Movie()`to instantiate movie objects. Each
movie has its own custom data structure defined by the move class and
constructor, and are stored in a list data structure. This list of movie
is what the `open_movies_page()` function needs as input in order to build the
HTML file, to display the website.
