#!/usr/bin/env python3
"""
Module for creating asyncio.Task
"""

import asyncio
from typing import Coroutine
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine with the given max_delay.

    Args:
        max_delay (int): Maximum delay value for wait_random in seconds.

    Returns:
        asyncio.Task: Task object for wait_random coroutine.
    """
    coro = wait_random(max_delay)
    task = asyncio.create_task(coro)
    return task

if __name__ == "__main__":
    # Test the task_wait_random function
    async def test(max_delay: int) -> None:
        task = task_wait_random(max_delay)
        await task
        print(task.__class__)

    asyncio.run(test(5))

