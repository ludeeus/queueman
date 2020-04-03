"""Example using taskfactory."""
import asyncio
from queueman.factory import QueueManager
from queueman.decorator import concurrent


@concurrent(2, 1)
async def exampletask(number):
    """Example task to run."""
    await asyncio.sleep(1)
    print(f"Test number: {number}")


async def example():
    """Run the example."""
    factory = QueueManager()
    for number in range(1, 10):
        factory.add(exampletask(number))

    while factory.pending_tasks != 0:
        await factory.execute(10)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())
