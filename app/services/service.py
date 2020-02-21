"""
Base service class.
"""

from abc import abstractmethod, ABC


class Service(ABC):
    """Base class for services."""

    @abstractmethod
    def setup(self):
        """Set up the service (e.g., connect to database)."""
        pass

    @abstractmethod
    def teardown(self):
        """Teardown the service (e.g., disconnect to database)."""
        pass
