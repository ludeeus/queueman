"""TaskFactory::exceptions"""


class TaskFactoryBaseException(Exception):
    """Base exception for TaskFactory."""


class TaskFactoryEmptyQueue(TaskFactoryBaseException):
    """Exception to raise if the queue is empty."""


class TaskFactoryExecutionStillInProgress(TaskFactoryBaseException):
    """Exception to raise if execution is still in progress."""
