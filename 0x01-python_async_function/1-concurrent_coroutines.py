#!/usr/bin/env python3
""" Task 1 """

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Wait_n """
    times: List[float] = []
    for i in range(n):
        times.append(wait_random(max_delay))
    return [await i for i in asyncio.as_completed(times)]
