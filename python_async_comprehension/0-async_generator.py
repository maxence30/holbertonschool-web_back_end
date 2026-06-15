#!/usr/bin/env python3
"""This module contains asynchronous utility functions."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return the generated delay."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay