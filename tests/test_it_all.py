"""Test everything."""
import pytest
from queueman import (
    QueueManager,
    QueueManagerExecutionStillInProgress,
    concurrent,
)


@concurrent(10)
async def dummy_task():
    """Dummy task."""


@concurrent(10)
def dummy_sync_task():
    """Dummy task."""


@pytest.mark.asyncio
async def test_everything():
    """Test everything."""
    queue = QueueManager()
    await queue.execute()
    assert not queue.running
    assert not queue.has_pending_tasks

    queue.add(dummy_task())
    assert queue.has_pending_tasks
    queue.clear()
    assert not queue.has_pending_tasks

    queue.running = True

    with pytest.raises(QueueManagerExecutionStillInProgress):
        await queue.execute()
    queue.running = False

    dummy_sync_task()

    queue.add(dummy_task())
    queue.add(dummy_task())
    await queue.execute(1)
    await queue.execute()
