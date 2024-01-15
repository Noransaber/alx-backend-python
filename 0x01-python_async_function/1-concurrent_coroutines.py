#!/usr/bin/env python3
"""
1. Let's execute multiple coroutines
at the same time with async
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without
    using sort() because of concurrency.
    """
    myList = []
    for i in range(0, n):
        res = await wait_random(max_delay)
        myList.append(res)
    sorted_list = sorted(myList)
    return sorted_list
