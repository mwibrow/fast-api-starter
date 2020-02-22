"""
Wrapper class for neo4j client.
"""

from aioneo4j import Neo4j

from .service import Service


class Neo4jService(Service):
    """Class managing a neo4j connection."""

    def __init__(self, host, port, username, password, loop=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.client = None

    async def start(self):
        """Set up Neo4j client."""
        self.client = Neo4j()
        self.client.__aenter__()

    async def stop(self):
        """Tear down Neo4J client."""
        await self.close()
