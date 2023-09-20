from lib.movies import *
import aiohttp
import pytest


@pytest.mark.asyncio
async def test_get_movie_id_function():
   async with aiohttp.ClientSession() as session:
        movie_id = await get_movie_id("Fight Club", session)
        assert movie_id == 550


@pytest.mark.asyncio
async def test_get_movie_title_function():
   async with aiohttp.ClientSession() as session:
        movie_title = await get_movie_title(550, session)
        assert movie_title == "Fight Club"