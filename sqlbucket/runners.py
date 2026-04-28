from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Connection
from sqlalchemy.pool import NullPool
from sqlbucket.utils import logger, sqlbucket_logo


class ProjectRunner:

    def __init__(
        self,
        configuration: dict,
        from_step: int = 1,
        to_step: int = None,
        verbose: bool = False,
        isolation_level: str = None
    ):
        pass

    def render_queries(self) -> None:
        pass

    def run_project(self) -> None:
        pass

    def starting_logs(self):
        pass

    def ending_logs(self, start, end):
        pass


def create_connection(
        configuration: dict, isolation_level: str = None) -> Connection:
    # todo: a user may prefer to run a session that commits data only at the
    #  very end of the ETL instead of an auto commit execution at engine level.

    # if no isolation level is indicated, we just create an engine without the
    # isolation level parameter. This means it will use the default one.
    # Check your backend DB documentation to know which one is the default as
    # it varies between databases.
    pass


def connection_query(configuration: dict, connection: Connection):
    pass
