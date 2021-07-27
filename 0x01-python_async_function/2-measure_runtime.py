#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time

    Args:
        n (int): spawn
        max_delay (int): max delay

    Returns:
        float: returns total_time / n
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    time_process = time.perf_counter() - start_time
    return time_process / n
