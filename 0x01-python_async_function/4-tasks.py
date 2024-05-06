#!/usr/bin/env python3
"""coroutine function asynchronous named wait_random"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Logic Function"""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    results = await asyncio.gather(*tasks)
    return sorted(results)
