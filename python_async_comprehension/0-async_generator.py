#!/usr/bin/env python3
"""Ce module définit une coroutine qui génère des nombres aléatoires de manière asynchrone."""

import asyncio
import random


async def async_generator()
"""Génère de manière asynchrone 10 nombres aléatoires entre 0 et 10 avec une pause d'une seconde."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
    