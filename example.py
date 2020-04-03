"""Example using taskfactory."""
import sys
import asyncio
import logging
from queueman import QueueManager, concurrent

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

HANDLER = logging.StreamHandler(sys.stdout)
HANDLER.setLevel(logging.DEBUG)
HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(HANDLER)


@concurrent(2, 1)
async def exampletask(number):
    """Example task to run."""
    await asyncio.sleep(1)
    logging.getLogger("example").info("Test number %s", str(number + 1))


async def example():
    """Run the example."""
    queue = QueueManager()
    for number in range(0, 10):
        queue.add(exampletask(number))

    while queue.has_pending_tasks:
        await queue.execute(5)


LOOP = asyncio.get_event_loop()
LOOP.run_until_complete(example())
