#!/usr/bin/env python3
"""Ce module exécute plusieurs tâches asynchrones simultanément."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Lance n tâches et retourne les délais dans l'ordre croissant."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    delays = []

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays