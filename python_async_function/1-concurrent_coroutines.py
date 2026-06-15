#!/usr/bin/env python3
"""Ce module exécute plusieurs coroutines simultanément."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Lance wait_random n fois et retourne les délais dans l'ordre croissant."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays