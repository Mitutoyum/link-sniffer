from selfcord.ext import commands
from selfcord import Message
from logging import getLogger

import re

logger = getLogger("bot")


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, message: Message, /) -> None:  # type: ignore
        if message.channel.id != 1168273280105459832 or not message.message_snapshots:
            return

        # r"(https?://\S+)"
        links = set(
            re.findall(
                r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
                message.message_snapshots[0].content,
            )
        )

        if links:
            for link in links:
                logger.info(link)
