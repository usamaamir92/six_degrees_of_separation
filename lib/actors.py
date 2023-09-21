import aiohttp
import asyncio

access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMTM5Nzc4MmRmZTJjZjM4NzAwNGE3NjdkMDg5MGNlZiIsInN1YiI6IjY1MDcwNmU4MTA5ZGVjMDE0ZjQxNDliZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.LCy0P7IlTe_dQ_s4cHj6Lw2ruwVGoM-RTqeRsofcyD8"
headers = {"Authorization": f"Bearer {access_token}"}

async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        if response.status != 200:
            raise Exception(f"Failed to fetch data. Status code: {response.status}")        
        return await response.json()
    


async def get_actor_id_from_search_string(search_string):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/search/person?query={search_string}&include_adult=false&language=en-US&page=1"
        data = await fetch(session, url)

        if len(data["results"]) != 0:
            actor_id = data["results"][0]["id"]
            return actor_id
        else:
            raise Exception("No actor found.")
        


async def get_actor_name_from_actor_id(actor_id):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.themoviedb.org/3/person/{actor_id}?language=en-US"
        data = await fetch(session, url)

        actor_name = data["name"]
        return actor_name
        

