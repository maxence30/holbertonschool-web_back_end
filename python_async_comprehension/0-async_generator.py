#!/usr/bin/env python

"""import des fonctions Asyincio"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Attend un délai aléatoire puis le retourne."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
