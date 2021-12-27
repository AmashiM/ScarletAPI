from scarlet import Scarlet
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()

from scarlet.scarletuser import ScarletUser

scarlet = Scarlet()

async def run():
    ai_token=os.environ["AI_TOKEN"]

    scarlet.set_user(ScarletUser.from_file())

    print(scarlet.current_user)

    res = await scarlet.sentience("Hello Bitch", ai_token=ai_token)
    
    

asyncio.run(run())