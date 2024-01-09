## Six Degrees of Separation

This is a project I've always wanted to work on. As a film buff I have always been curious if certain actors appear in any movies with another actor. This functionality already exists on the IMDB website and on Oracle of Bacon, but it would be fun to try and implement myself.

Initially I will try to build this purely by calling the TMDB API and no database, but I suspect with longer chains this will affect performance hence may need to switch to a database model eventually. No user login/authentication functionality required.

Since this project is mostly comprised of back-end logic and limited front-end requirements, I will use a basic Flask template and CSS for styling. This is also a good opportunity to try asynchronous programming in Python as I have only used async functions in Javascript previously.
