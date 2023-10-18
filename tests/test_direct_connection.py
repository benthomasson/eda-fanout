"""

test_emitter_alone() checks that the emitter can be run alone.
test_emitter_with_source() checks that the emitter can be run with a source.

"""


import emitter1
import pytest
import asyncio
import source1


@pytest.mark.asyncio
async def test_emitter_alone():
    """
    This test checks that the emitter can be run alone.
    Sends 100 messages to the emitter, then sends None to the emitter.
    """
    queue = asyncio.Queue()
    args = {}
    emitter = asyncio.create_task(emitter1.main(queue, args))
    for i in range(100):
        await queue.put(f"test{i}")
    await queue.put(None)
    # And wait for the emitter to finish
    await emitter


@pytest.mark.asyncio
async def test_emitter_with_source():
    """
    This test checks that the emitter can be run with a source.
    The source sends 100 messages to the emitter, then the test sends None to the emitter
    to shut it down.
    """
    queue = asyncio.Queue()
    source_args = {"limit": 100}
    emitter_args = {}
    source = asyncio.create_task(source1.main(queue, source_args))
    emitter = asyncio.create_task(emitter1.main(queue, emitter_args))
    # Let the source finish
    await source
    # Then send the None to the emitter
    await queue.put(None)
    # And wait for the emitter to finish
    await emitter
