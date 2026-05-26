#Day 96 - asyncio Module 
import asyncio

async def task(name, delay):
    print(f"{name} starting")
    await asyncio.sleep(delay)
    print(f"{name} done")

async def main():
    await asyncio.gather(
        task("Task-1", 1),
        task("Task-2", 2),
        task("Task-3", 1.5)
    )

if __name__ == "__main__":
    asyncio.run(main())