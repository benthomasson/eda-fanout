

import emitter1
import pytest
import asyncio
import source1

@pytest.mark.asyncio
async def test_emitter_alone():
    queue = asyncio.Queue()
    args = {}
    emitter = asyncio.create_task(emitter1.main(queue, args))
    for i in range(100):
        await queue.put(f'test{i}')
    await queue.put(None)
    # And wait for the emitter to finish
    await emitter


@pytest.mark.asyncio
async def test_emitter_with_source():
    queue = asyncio.Queue()
    source_args = {'limit': 100}
    emitter_args = {}
    source = asyncio.create_task(source1.main(queue, source_args))
    emitter = asyncio.create_task(emitter1.main(queue, emitter_args))
    # Let the source finish
    await source
    # Then send the None to the emitter
    await queue.put(None)
    # And wait for the emitter to finish
    await emitter

