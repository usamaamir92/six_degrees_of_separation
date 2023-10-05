from lib.actors import *
import aiohttp
import pytest


@pytest.mark.asyncio
async def test_get_actor_id_from_search_string_function():
      actor_id = await get_actor_id_from_search_string("Brad Pitt")
      assert actor_id == 287



@pytest.mark.asyncio
async def test_get_actor_id_function_with_fake_actor():
   with pytest.raises(Exception) as e:
      actor_id = await get_actor_id_from_search_string("Fake Actor")
      assert str(e.value) == "No actor found."



#Only testing for valid IDs as this function won't be called directly by the user.
@pytest.mark.asyncio
async def test_get_actor_name_from_actor_id_function():
      actor_name = await get_actor_name_from_actor_id(287)
      assert actor_name == "Brad Pitt"



@pytest.mark.asyncio
async def test_get_list_of_movie_ids_from_actor_id_function():
      list_of_movie_ids = await get_list_of_movie_ids_from_actor_id(287)
      assert list_of_movie_ids[0:6] == [297, 652, 787, 978, 1164, 4476]