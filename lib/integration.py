import aiohttp
import asyncio
from lib.actors import *
from lib.movies import *

access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTM5Nzc4MmRmZTJjZjM4NzAwNGE3NjdkMDg5MGNlZiIsInN1YiI6IjY1MDcwNmU4MTA5ZGVjMDE0ZjQxNDliZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LCy0P7IlTe_dQ_s4cHj6Lw2ruwVGoM-RTqeRsofcyD8"
headers = {"Authorization": f"Bearer {access_token}"}

async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status != 200:
            raise Exception(f"Failed to fetch data. Status code: {response.status}")        
        return await response.json()



async def get_associated_actors_for_actor_id(actor_id):
    async with aiohttp.ClientSession() as session:
        associated_actors = []

        movies_list = await get_list_of_movie_ids_from_actor_id(actor_id)
        for movie in movies_list:
            actors = await get_list_of_actor_ids_from_movie_id(movie)
            associated_actors.extend(actors)
        
        associated_actors =list(set(associated_actors))
        return associated_actors
    


async def is_common_movie(actor1_id, actor2_id):
    async with aiohttp.ClientSession() as session:
        actor1_movies = await get_list_of_movie_ids_from_actor_id(actor1_id)
        for movie_id in actor1_movies:
            actors_in_movie = await get_list_of_actor_ids_from_movie_id(movie_id)
            if actor2_id in actors_in_movie:
                return True
        return False



# async def find_common_movie(actor1_id, actor2_id):
#     async with aiohttp.ClientSession() as session:
#         actor1_name = await get_actor_name_from_actor_id(actor1_id)
#         actor2_name = await get_actor_name_from_actor_id(actor2_id)

#         # chain = []
#         if await is_common_movie(actor1_id,actor2_id) == True:
#             actor1_movies = await get_list_of_movie_ids_from_actor_id(actor1_id)
#             for movie_id in actor1_movies:
#                 actors_in_movie = await get_list_of_actor_ids_from_movie_id(movie_id)
#                 if actor2_id in actors_in_movie:
#                     common_movie_title = await get_movie_title_from_movie_id(movie_id)
#                     return common_movie_title
#         else:
#             return "No common movies!"
    

async def find_actors_link(actor1_id, actor2_id):
    async with aiohttp.ClientSession() as session:
        associated_actors = await get_associated_actors_for_actor_id(actor1_id)
        if actor2_id in associated_actors:
            return "X and Y both star in Z"
        for actor in associated_actors:
            return 



async def find_common_movie(actor1_id, actor2_id, depth=0):
    if depth > 2:
        return "No common movies"

    async with aiohttp.ClientSession() as session:
        actor1_name = await get_actor_name_from_actor_id(actor1_id)
        actor2_name = await get_actor_name_from_actor_id(actor2_id)

        # chain = []

        actor1_movies = await get_list_of_movie_ids_from_actor_id(actor1_id)
        for movie_id in actor1_movies:
            actors_in_movie = await get_list_of_actor_ids_from_movie_id(movie_id)
            print(actors_in_movie)
            if actor2_id in actors_in_movie:
                common_movie_title = await get_movie_title_from_movie_id(movie_id)
                return common_movie_title
                # chain.append([actor1_name, common_movie_title, actor2_name])
                # if len(chain) > 0:
                    # break
        
        associated_actors = await get_associated_actors_for_actor_id(actor1_id)
        for actor_id in associated_actors:
            result = await find_common_movie(actor_id, actor2_id, depth + 1)
            if result != "No common movies":
                return result
            
        return "No common movies"
        # return "No common movie"
        # if len(chain) == 0:
        #     associated_actors = await get_associated_actors_for_actor_id(actor1_id)
        #     for actor_id in associated_actors:
        #         await find_common_movie(actor_id, actor2_id)

        # return common_movie_title
    


loop = asyncio.get_event_loop()
# print(loop.run_until_complete(get_movie_id_from_search_string("Fight Club")))
print(loop.run_until_complete(get_list_of_movie_ids_from_actor_id(287)))
print(loop.run_until_complete(get_list_of_actor_ids_from_movie_id(297)))
print(loop.run_until_complete(get_associated_actors_for_actor_id(287)))
