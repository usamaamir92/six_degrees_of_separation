from lib.actors import *
import aiohttp
import pytest


@pytest.mark.asyncio
async def test_get_actor_id_function():
   async with aiohttp.ClientSession() as session:
        actor_id = await get_actor_id("Brad Pitt", session)
        assert actor_id == 287



@pytest.mark.asyncio
async def test_get_actor_id_function_with_fake_actor():
   async with aiohttp.ClientSession() as session:
      with pytest.raises(Exception) as e:
         actor_id = await get_actor_id("Fake Actor", session)
         assert str(e.value) == "No actor found."



#Only testing for valid IDs as this function won't be called directly by the user.
@pytest.mark.asyncio
async def test_get_actor_name_function():
   async with aiohttp.ClientSession() as session:
        actor_name = await get_actor_name(287, session)
        assert actor_name == "Brad Pitt"