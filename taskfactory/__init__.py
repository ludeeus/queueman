"""Initalize taskfactory."""
from taskfactory.factory import TaskFactory
from taskfactory.exceptions import (
    TaskFactoryBaseException,
    TaskFactoryEmptyQueue,
    TaskFactoryExecutionStillInProgress,
)
