#!/usr/bin/env python3
""" Task 4 """

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n """
    times: List[float] = []
    for i in range(n):
        times.append(task_wait_random(max_delay))
    return [await i for i in asyncio.as_completed(times)]
