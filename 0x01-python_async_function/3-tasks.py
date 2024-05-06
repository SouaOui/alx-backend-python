#!/usr/bin/env python3
"""coroutine function asynchronous named wait_random"""
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> Task:
    """spawn wait_random n times with the specified max_delay."""
    return asyncio.Task(wait_random(max_delay))