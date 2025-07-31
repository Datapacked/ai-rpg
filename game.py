import art

a = art.text2art("AI  RPG", font='medium', space=1)

print(a)

import time, asyncio

async def fun():
	await asyncio.sleep(4)
	return False

