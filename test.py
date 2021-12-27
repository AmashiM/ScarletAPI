from scarlet import Scarlet, ScarletUser
from dotenv import load_dotenv
import asyncio
import os
load_dotenv()


async def run():
    scarlet = Scarlet(
        user=ScarletUser.from_file(".user.json")
    )

    ai_token=os.environ["AI_TOKEN"]

    print(scarlet.current_user)

    res = await scarlet.sentience("Hello BitchAss Cynt", ai_token=ai_token)
    print(res.raw)
    
    
asyncio.run(run())