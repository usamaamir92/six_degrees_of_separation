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
        movies_list = await get_list_of_movie_ids_from_actor_id(actor_id)

        # Fetch associated actors concurrently
        tasks = [get_list_of_actor_ids_from_movie_id(movie) for movie in movies_list]
        actors_lists = await asyncio.gather(*tasks)

        # Flatten list and remove duplicates
        associated_actors = list(set(actor for actors_list in actors_lists for actor in actors_list))
        return associated_actors


async def is_common_movie(actor1_id, actor2_id):
    async with aiohttp.ClientSession() as session:
        actor1_associated_actors = await get_associated_actors_for_actor_id(actor1_id)
        if actor2_id in actor1_associated_actors:
            return True
        else:
            return False
    

# async def find_actors_link(actor1_id, actor2_id):
#     async with aiohttp.ClientSession() as session:
#         associated_actors = await get_associated_actors_for_actor_id(actor1_id)
#         if actor2_id in associated_actors:
#             return "X and Y both star in Z"
#         for actor in associated_actors:
#             return 



# async def find_common_movie(actor1_id, actor2_id, depth=0):
#     async with aiohttp.ClientSession() as session:
#         actor1_name = await get_actor_name_from_actor_id(actor1_id)
#         actor2_name = await get_actor_name_from_actor_id(actor2_id)

#         order1_associated_actors = await get_associated_actors_for_actor_id(actor1_id)
#         if actor2_id in order1_associated_actors:
#             return "Yes"
#         else:
#             order2_associated_actors = []
#             for actor in order1_associated_actors:
#                 order2_associated_actors.append(await get_associated_actors_for_actor_id(actor))
#             # order2_associated_actors = list((order2_associated_actors)
#             return order2_associated_actors


async def find_common_movie_title(actor1_id, actor2_id):
    async with aiohttp.ClientSession() as session:

        actor1_movies = await get_list_of_movie_ids_from_actor_id(actor1_id)
        for movie_id in actor1_movies:
            actors_in_movie = await get_list_of_actor_ids_from_movie_id(movie_id)
            if actor2_id in actors_in_movie:
                common_movie_title = await get_movie_title_from_movie_id(movie_id)
                return common_movie_title
            else:
                return "No common movie!"
        return None



async def find_actors_link(actor1_id, actor2_id, chain=[], depth=0):
    if depth > 1:
        return "No common movies in 2 links"
    
    async with aiohttp.ClientSession() as session:
        actor1_name = await get_actor_name_from_actor_id(actor1_id)
        actor2_name = await get_actor_name_from_actor_id(actor2_id)

        common_movie = await find_common_movie_title(actor1_id, actor2_id)
        if common_movie != None:
            chain.extend([actor1_name, common_movie, actor2_name])
            return chain
        associated_actors = await get_associated_actors_for_actor_id(actor1_id)
        for actor_id in associated_actors:
            return await find_actors_link(actor_id, actor2_id, depth+1)


loop = asyncio.get_event_loop()
# print(loop.run_until_complete(get_movie_id_from_search_string("Fight Club")))
print(loop.run_until_complete(get_list_of_movie_ids_from_actor_id(287)))
print(loop.run_until_complete(get_list_of_actor_ids_from_movie_id(297)))
print(loop.run_until_complete(get_associated_actors_for_actor_id(287)))
