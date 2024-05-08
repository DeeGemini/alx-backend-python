#!/usr/bin/env python3
"""
Module for measuring runtime of wait_n coroutine
"""

import time
from typing import List
from concurrent.futures import ThreadPoolExecutor
from asyncio import run, gather
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return average time per execution.

    Args:
        n (int): Number of times to run wait_n.
        max_delay (int): Maximum delay value for wait_n in seconds.

    Returns:
        float: Average time per execution in seconds.
    """
    start_time = time.time()

    async def run_wait_n():
        return await wait_n(n, max_delay)

    async def main():
        await run(run_wait_n())

    run(main())

    end_time = time.time()
    total_time = end_time - start_time
    avg_time_per_execution = total_time / n
    return avg_time_per_execution

if __name__ == "__main__":
    # Test the measure_time function
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))

