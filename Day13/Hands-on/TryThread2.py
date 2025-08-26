import asyncio
import aiohttp
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5"
]

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            data = await response.text()
            print(f"Fetched from {url} with status {response.status}")
            return data
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    results = asyncio.run(fetch_all(urls))

    for i, content in enumerate(results):
        print(f"\n--- Content from URL {i + 1} ---\n{content[:100]}...") 