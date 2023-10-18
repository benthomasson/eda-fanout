import asyncio
from typing import Any, Dict


async def main(queue: asyncio.Queue, args: Dict[str, Any]):
    delay = args.get("delay", 0)

    while True:
        message = await queue.get()
        if message is None:
            break
        print(message)
