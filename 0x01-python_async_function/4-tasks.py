#!/usr/bin/python3
"""Defines an asynchronous coroutine"""


import asyncio
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    """Spawns task_wait_random n times with the specified max_delay"""
    return await asyncio.gather(*(task_wait_random(max_delay)
                                  for i in range(n)))
