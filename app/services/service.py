"""
Base service class.
"""

from abc import abstractmethod, ABC


class Service(ABC):
    """Base class for services."""

    @abstractmethod
    async def startup(self):
        """Set up the service (e.g., connect to database)."""
        pass

    @abstractmethod
    async def shutdown(self):
        """Teardown the service (e.g., disconnect to database)."""
        pass
