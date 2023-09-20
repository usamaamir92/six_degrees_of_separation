from lib.movies import *
import aiohttp
import pytest



@pytest.mark.asyncio
async def test_get_movie_id_function():
   async with aiohttp.ClientSession() as session:
        movie_id = await get_movie_id_from_search_string("Fight Club", session)
        assert movie_id == 550



@pytest.mark.asyncio
async def test_get_movie_id_function_with_fake_movie():
   async with aiohttp.ClientSession() as session:
         with pytest.raises(Exception) as e:
           movie_id = await get_movie_id_from_search_string("Very Fake Movie", session)
           assert str(e.value) == "No movie found."



#Only testing for valid IDs as this function won't be called directly by the user.
@pytest.mark.asyncio
async def test_get_movie_title_function():
   async with aiohttp.ClientSession() as session:
        movie_title = await get_movie_title_from_movie_id(550, session)
        assert movie_title == "Fight Club"



@pytest.mark.asyncio
async def test_get_list_of_movie_ids_from_actor_id():
   async with aiohttp.ClientSession() as session:
        list_of_movie_ids = await get_list_of_movie_ids_from_actor_id(287, session)
        assert list_of_movie_ids[0:6] == [297, 652, 787, 978, 1164, 4512]