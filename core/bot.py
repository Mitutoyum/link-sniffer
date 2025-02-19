from selfcord.ext import commands
from selfcord import Message
from logging import getLogger
from core.utils import config_manager, sniff

logger = getLogger("bot")


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, message: Message, /) -> None:  # type: ignore
        sniff_type = config_manager.get_flag("sniff_type")

        if sniff_type == "global":
            content = message.content
        elif sniff_type == "server":
            server_id = config_manager.get_flag("server_id")

            if message.guild_id == server_id:
                content = message.content
        elif sniff_type == "channel_id":
            channel_id = config_manager.get_flag("channel_id")
            if message.channel.id == channel_id:
                content = message.content
        else:
            return

        links = sniff.sniff_re(content)  # type: ignore

        if links:
            for link in links:
                logger.info(link)
