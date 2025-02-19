import re

from selfcord import Message


def sniff_re(content: str) -> set[str] | None:
    links = set(
        re.findall(
            r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
            content,
        )
    )

    return links
