#!/usr/bin/env python3
# async.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")


asyncio.run(count())
