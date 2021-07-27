#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time

    Args:
        n (int): spawn
        max_delay (int): max delay

    Returns:
        float: returns total_time / n
    """
    t1 = time.perf_counter()
    new_list = asyncio.run(wait_n(n, max_delay))
    t2 = time.perf_counter()
    return (t2 - t1) / n
