import asyncio



async def printer():
    for i in range(3):
        print(i)


async def async_print(text):
    print(text)

async def main():
    task1=asyncio.create_task(printer())
    #await printer()
    task2=asyncio.create_task(async_print("hello world"))
    await task2


asyncio.run(main())