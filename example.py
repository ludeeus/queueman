"""Example using taskfactory."""
import asyncio
from queueman import QueueManager, concurrent


@concurrent(2, 1)
async def exampletask(number):
    """Example task to run."""
    await asyncio.sleep(1)
    print(f"Test number: {number}")


async def example():
    """Run the example."""
    queue = QueueManager()
    for number in range(1, 10):
        queue.add(exampletask(number))

    while queue.has_pending_tasks:
        await queue.execute(10)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())
