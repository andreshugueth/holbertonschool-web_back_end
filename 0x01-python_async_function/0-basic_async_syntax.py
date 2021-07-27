#!/usr/bin/env python3
""" The basics of async """
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """asynchronous coroutine

    Args:
        max_delay (int): [description]

    Returns:
        Union[int, float]: [description]
    """
    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
