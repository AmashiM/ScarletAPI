from requests.sessions import extract_cookies_to_jar
from scarlet import Scarlet, ScarletUser
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()


async def run():
    print("started")
    scarlet = Scarlet()
    scarlet.set_user(ScarletUser.from_file(".user.json"))

    user = scarlet.sync_get_user(scarlet.current_user.uid, timeout=3)
    print(user)


    
loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(run())
except Exception as err:
    print(err)
    loop.close()
    exit()