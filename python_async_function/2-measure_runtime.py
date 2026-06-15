#!/usr/bin/env python3
"""Ce module mesure le temps moyen d'exécution des coroutines."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Mesure le temps moyen d'exécution de wait_n."""
    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    end = time.time()

    return (end - start) / n