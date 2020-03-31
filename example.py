"""Example using taskfactory."""
import asyncio
from taskfactory.factory import TaskFactory


async def exampletask(number):
    """Example task to run."""
    await asyncio.sleep(1)
    print(f"Test number: {number}")


async def example():
    """Run the example."""
    factory = TaskFactory()
    for number in range(1, 20):
        factory.add(exampletask(number))

    while factory.pending_tasks != 0:
        await factory.execute(5)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())
