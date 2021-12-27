from scarlet import Scarlet, ScarletUser
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()


async def run():
    scarlet = Scarlet(
        user=ScarletUser.from_file(".user.json")
    )

    res = await scarlet.docs()
    print(res)
    
    
asyncio.run(run())