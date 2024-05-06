#!/usr/bin/env python3
"""coroutine function asynchronous named wait_random"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """the function logic"""
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
