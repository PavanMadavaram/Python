#Day 96 - Async Helper
import asyncio

async def countdown(n):
    while n > 0:
        print(n)
        await asyncio.sleep(0.2)
        n -= 1

asyncio.run(countdown(3))
print("Helper complete")