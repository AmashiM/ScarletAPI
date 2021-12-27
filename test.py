from requests.sessions import extract_cookies_to_jar
from scarlet import Scarlet, ScarletUser
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()


async def run():
    user = await Scarlet.create("Amashi", "JEM139851", "amashisenpai386@gmail.com")
    print(user)
    
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(run())
except Exception as err:
    print(err)
    loop.close()
    exit()