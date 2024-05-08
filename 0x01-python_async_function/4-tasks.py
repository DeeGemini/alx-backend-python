#!/usr/bin/env python3
"""
Module for creating asyncio.Task for multiple coroutines
"""

import asyncio
from typing import List
from asyncio import Task
from 3-tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn asyncio.Tasks using task_wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn task_wait_random.
        max_delay (int): Maximum delay value for task_wait_random in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks: List[Task] = []
    delays: List[float] = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return sorted(delays)

if __name__ == "__main__":
    # Test the task_wait_n function
    async def test_task_wait_n(n: int, max_delay: int) -> None:
        delays = await task_wait_n(n, max_delay)
        print(delays)

    asyncio.run(test_task_wait_n(5, 6))

