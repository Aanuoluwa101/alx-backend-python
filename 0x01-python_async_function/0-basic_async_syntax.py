#!/usr/bin/env python3
"""Defines an asynchronous coroutine"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
