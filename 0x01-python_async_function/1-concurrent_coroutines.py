#!/usr/bin/python3
"""Defines an asynchronous coroutine"""


import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n, max_delay):
    """Spawns wait_random n times with the specified max_delay"""
    return await asyncio.gather(*(wait_random(max_delay) for i in range(n)))