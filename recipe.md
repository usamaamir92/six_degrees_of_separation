MVP:

----------------------------------------------
- Degrees of separation between actors
----------------------------------------------

User enters two search strings: actor1 and actor2. "Degree of separation" is returned showing movie(s) they are linked by. If not linked within 6 links, return "no link within 5 connections".


Some basic API call methods will first be required to get movie/actor ids from search strings, before the larger function can be built.

---------------
Function:
Get actor id from search string

Arguments:
Search string

Returns:
Actor id if actor exists
Error "No actor found" if error
---------------


---------------
Function:
Get movie id from search string

Arguments:
Search string

Returns:
Movie id if movie exists
Error "No movie found" if error
---------------


---------------
Function:
Get actor name from actor id

Arguments:
actor id

Returns:
Actor name if actor exists
Error "No actor found" if error
---------------


---------------
Function:
Get movie name from movie id

Arguments:
movie id

Returns:
Movie name if movie exists
Error "No movie found" if error
---------------