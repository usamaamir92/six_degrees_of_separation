import aiohttp
import asyncio

access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTM5Nzc4MmRmZTJjZjM4NzAwNGE3NjdkMDg5MGNlZiIsInN1YiI6IjY1MDcwNmU4MTA5ZGVjMDE0ZjQxNDliZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LCy0P7IlTe_dQ_s4cHj6Lw2ruwVGoM-RTqeRsofcyD8"



async def get_movie_id_from_search_string(search_string, session):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/search/movie?query={search_string}&include_adult=false&language=en-US&page=1"
        
        async with session.get(url, headers={"Authorization": f"Bearer {access_token}"}) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data. Status code: {response.status}")        

            data = await response.json()
            if len(data["results"]) != 0:
                movie_id = data["results"][0]["id"]
                return movie_id
            else:
                raise Exception("No movie found.")



async def get_movie_title_from_movie_id(movie_id, session):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        
        async with session.get(url, headers={"Authorization": f"Bearer {access_token}"}) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data. Status code: {response.status}")

            data = await response.json()
            movie_title = data["title"]
            return movie_title



async def get_list_of_movie_ids_from_actor_id(actor_id, session):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/person/{actor_id}/movie_credits?language=en-US"

        async with session.get(url, headers={"Authorization": f"Bearer {access_token}"}) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch data. Status code: {response.status}")

            data = await response.json()
            list_of_movie_ids = [movie["id"] for movie in data["cast"] if "title" in movie.keys()]
            return list_of_movie_ids