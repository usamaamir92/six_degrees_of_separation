import aiohttp
import asyncio

access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTM5Nzc4MmRmZTJjZjM4NzAwNGE3NjdkMDg5MGNlZiIsInN1YiI6IjY1MDcwNmU4MTA5ZGVjMDE0ZjQxNDliZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LCy0P7IlTe_dQ_s4cHj6Lw2ruwVGoM-RTqeRsofcyD8"


async def get_movie_id(search_string, session):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/search/movie?query={search_string}&include_adult=false&language=en-US&page=1"
        async with session.get(url, headers={"Authorization": f"Bearer {access_token}"}) as response:
            data = await response.json()
            movie_id = data["results"][0]["id"]
            return movie_id


async def get_movie_title(movie_id, session):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        async with session.get(url, headers={"Authorization": f"Bearer {access_token}"}) as response:
            data = await response.json()
            movie_title = data["title"]
            return movie_title