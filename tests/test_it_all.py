"""Test everything."""
import pytest
from taskfactory import (
    TaskFactory,
    TaskFactoryEmptyQueue,
    TaskFactoryExecutionStillInProgress,
)


async def dummy_task():
    """Dummy task."""


@pytest.mark.asyncio
async def test_everything():
    """Test everything."""
    factory = TaskFactory()
    assert not factory.running
    assert factory.pending_tasks == 0

    factory.add(dummy_task())
    assert factory.pending_tasks != 0
    factory.clear()
    assert factory.pending_tasks == 0

    with pytest.raises(TaskFactoryEmptyQueue):
        await factory.execute()

    factory.running = True
    with pytest.raises(TaskFactoryExecutionStillInProgress):
        await factory.execute()

    factory.running = False
    factory.add(dummy_task())
    factory.add(dummy_task())
    await factory.execute(1)
    await factory.execute()
