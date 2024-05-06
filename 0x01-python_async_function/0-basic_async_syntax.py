#!/usr/bin/env python3
"""coroutine function asynchronous named wait_random"""
import random


async def wait_random(max_delay=10):
    """the function logic"""
    return random.uniform(0, max_delay)
