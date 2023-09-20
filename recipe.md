MVP:

----------------------------------------------
- Degrees of separation between actors
----------------------------------------------

User enters two search strings: actor1 and actor2. "Degree of separation" is returned showing movie(s) they are linked by. If not linked within 6 links, return "no link within 5 connections".


Some basic API call methods will first be required to get movie/actor ids from search strings, before the larger function can be built.

---------------
Function:
Get actor/movie id from search string

Arguments:
Search string

Returns:
Actor/movie id if actor exists
Error "No actor/movie found" if error
---------------


---------------
Function:
Get actor/movie name from id

Arguments:
actor/movie id

Returns:
Actor/movie name if exists
Error "No actor/movie found" if error
---------------

Next, we will need to get a list of movies for a given actor id. Movie details (title) and credits both take movie id as input, so we will output movies as ids.

---------------
Function:
Get list of movie ids for actor id.

Arguments:
actor id

Returns:
List of movie ids
Error "No movies found" if error
---------------