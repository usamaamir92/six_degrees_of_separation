from lib.movies import *
from lib.integration import *
import aiohttp
import pytest



# @pytest.mark.asyncio
# async def test_get_associated_actors_function():
#     associated_actors = await get_associated_actors_for_actor_id(287)
#     # print(len(associated_actors))
#     assert associated_actors[0:4] == [1163266, 3, 4, 2]




@pytest.mark.asyncio
async def test_find_common_movie_function():
    # 287 = Brad Pitt, 4173 = Anthony Hopkins
    common_movie = await find_common_movie_title(287,4173)
    assert common_movie == 'Meet Joe Black'


@pytest.mark.asyncio
async def test_find_common_movie_function():
    # 287 = Brad Pitt, 4173 = Anthony Hopkins
    common_movie = await find_common_movie_title(287,1158)
    assert common_movie == 'No common movie!'


# @pytest.mark.asyncio
# async def test_is_common_movie_function():
#     common_movie = await is_common_movie(287, 4173)
#     assert common_movie == True


# @pytest.mark.asyncio
# async def test_find_actors_link():
#     common_movie = await find_actors_link(287,1159)
#     assert common_movie == ['Brad Pitt', 'Meet Joe Black', 'Anthony Hopkins']



# @pytest.mark.asyncio
# async def test_is_common_movie_function():
#     assert await is_common_movie(287,1158) == True

#  1158 = Al Pacino