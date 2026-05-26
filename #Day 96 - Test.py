#Day 96 - Test
import asyncio

async def hello():
    return "ok"

result = asyncio.run(hello())
print("Async test:", result == "ok")
print("Day 96 test ok")