

import emitter1
import pytest
import asyncio

@pytest.mark.asyncio
async def test_1():
    queue = asyncio.Queue()
    args = {}
    emitter = asyncio.create_task(emitter1.main(queue, args))
    for i in range(100):
        await queue.put(f'test{i}')
    await queue.put(None)
    await emitter

