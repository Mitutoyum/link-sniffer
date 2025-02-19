import selfcord
import dotenv
import asyncio
import logging
import os

from core.bot import Bot

selfcord.utils.setup_logging(root=True)

filehandler = logging.FileHandler("records.txt", encoding="utf-8")

logger = logging.getLogger("bot")
logger.addHandler(filehandler)


async def main():
    bot = Bot(command_prefix="", self_bot=True)

    dotenv.load_dotenv()

    await bot.start(os.getenv("TOKEN"))  # type: ignore


if __name__ == "__main__":
    asyncio.run(main())
