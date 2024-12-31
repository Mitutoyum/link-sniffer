import selfcord
import logging

from asyncio import run
from os import getenv
from dotenv import load_dotenv
from core.bot import Bot

selfcord.utils.setup_logging(root=True)

filehandler = logging.FileHandler("records.txt", encoding="utf-8")

logger = logging.getLogger("bot")
logger.addHandler(filehandler)


async def main():
    bot = Bot(command_prefix="", self_bot=True)

    load_dotenv()

    await bot.start(getenv("TOKEN"))  # type: ignore


if __name__ == "__main__":
    run(main())
