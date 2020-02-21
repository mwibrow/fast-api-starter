"""
Wrapper class for neo4j client.
"""


from .service import Service


class Neo4j(Service):
    """Class managing a neo4j connection."""

    def __init__(self, host, port):
        self.host = host
        self.port = port
