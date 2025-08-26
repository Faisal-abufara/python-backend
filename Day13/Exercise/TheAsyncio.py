import asyncio
import random

async def download_file(file_name):
    print(f"Starting download of {file_name}...")
    download_time = random.randint(1, 5)
    await asyncio.sleep(download_time)
    print(f"Finished downloading {file_name} in {download_time} seconds.")

async def main():
    files = ["file1.txt", "file2.mp4", "file3.jpg", "file4.pdf", "file5.zip"]
    tasks = [asyncio.create_task(download_file(file)) for file in files]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
