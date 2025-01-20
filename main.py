import asyncio
from main_bot import SingpassBot

bot = SingpassBot()
async def main():
    await bot.run()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

