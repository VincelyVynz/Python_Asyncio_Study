import asyncio, aiohttp,os

urls = ["https://images.pexels.com/photos/31001122/pexels-photo-31001122.jpeg",
        "https://images.pexels.com/photos/32838311/pexels-photo-32838311.jpeg",
        "https://images.pexels.com/photos/6415078/pexels-photo-6415078.jpeg",
        "https://www.pexels.com/download/video/1583096.mp4",
        "https://www.pexels.com/download/video/9885661.mp4"]

# Sample images and video URLs used in this project are from Pexels (https://www.pexels.com)


save_folder = "downloaded_images"
os.makedirs(save_folder,exist_ok=True)

async def download_images(session, url):
    filename = os.path.join(save_folder, os.path.basename(url))
    print('Starting download of ' + filename)
    async with session.get(url) as response:
        content = await response.read()
        with open(filename, 'wb') as f:
            f.write(content)
    print('Finished downloading ' + filename)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [download_images(session, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())