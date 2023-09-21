import asyncio
import aiohttp



access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTM5Nzc4MmRmZTJjZjM4NzAwNGE3NjdkMDg5MGNlZiIsInN1YiI6IjY1MDcwNmU4MTA5ZGVjMDE0ZjQxNDliZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LCy0P7IlTe_dQ_s4cHj6Lw2ruwVGoM-RTqeRsofcyD8"
headers = {"Authorization": f"Bearer {access_token}"}

async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status != 200:
            raise Exception(f"Failed to fetch data. Status code: {response.status}")        
        return await response.json()



async def get_movie_id_from_search_string(search_string):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/search/movie?query={search_string}&include_adult=false&language=en-US&page=1"
        data = await fetch(session, url)

        if len(data["results"]) != 0:
            movie_id = data["results"][0]["id"]
            return movie_id
        else:
            raise Exception("No movie found.")



async def get_movie_title_from_movie_id(movie_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        data = await fetch(session, url)

        movie_title = data["title"]
        return movie_title



async def get_list_of_movie_ids_from_actor_id(actor_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/person/{actor_id}/movie_credits?language=en-US"
        data = await fetch(session, url)

        list_of_movie_ids = [movie["id"] for movie in data["cast"] if "title" in movie.keys()]
        return list_of_movie_ids
        


async def get_list_of_actor_ids_from_movie_id(movie_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
        movie_data = await fetch(session, url)

        list_of_actor_ids = [actor["id"] for actor in movie_data["cast"] if actor["known_for_department"] == "Acting"]
        return list_of_actor_ids


# loop = asyncio.get_event_loop()
# print(loop.run_until_complete(get_movie_id_from_search_string("Fight Club")))
# print(loop.run_until_complete(get_list_of_actor_ids_from_movie_id(297)))