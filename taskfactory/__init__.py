"""Initalize taskfactory."""
from taskfactory.factory import TaskFactory
from taskfactory.exceptions import (
    TaskFactoryBaseException,
    TaskFactoryEmptyQueue,
    TaskFactoryExecutionStillInProgress,
)
from taskfactory.helper import iscoroutine
from taskfactory.decorator import concurrent
