"""Test everything."""
import pytest
from queueman import (
    QueueManager,
    QueueManagerEmptyQueue,
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
    assert not queue.running
    assert queue.pending_tasks == 0

    queue.add(dummy_task())
    assert queue.pending_tasks != 0
    queue.clear()
    assert queue.pending_tasks == 0

    with pytest.raises(QueueManagerEmptyQueue):
        await queue.execute()

    queue.running = True
    with pytest.raises(QueueManagerExecutionStillInProgress):
        await queue.execute()

    dummy_sync_task()
    queue.running = False
    queue.add(dummy_task())
    queue.add(dummy_task())
    await queue.execute(1)
    await queue.execute()
