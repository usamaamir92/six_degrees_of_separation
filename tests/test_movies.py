from lib.movies import *
# import aiohttp
import pytest



@pytest.mark.asyncio
async def test_get_movie_id_from_search_string_function():
   movie_id = await get_movie_id_from_search_string("Fight Club")
   assert movie_id == 550



@pytest.mark.asyncio
async def test_get_movie_id_function_with_fake_movie():
      with pytest.raises(Exception) as e:
         movie_id = await get_movie_id_from_search_string("Very Fake Movie")
         assert str(e.value) == "No movie found."



#Only testing for valid IDs as this function won't be called directly by the user.
@pytest.mark.asyncio
async def test_get_movie_title_from_movie_id_function():
      movie_title = await get_movie_title_from_movie_id(550)
      assert movie_title == "Fight Club"



@pytest.mark.asyncio
async def test_get_list_of_actor_ids_from_movie_id():
      list_of_actor_ids = await get_list_of_actor_ids_from_movie_id(297)
      assert list_of_actor_ids == [287, 4173, 4174, 4177, 
                                    4726, 4175, 35515, 21382, 
                                    1716582, 117379, 4192, 
                                    4193, 4194, 4195, 1661585, 
                                    57823, 1254683]