from sqlbucket.runners import create_connection, connection_query
from sqlbucket.runners import logger
from tabulate import tabulate
from sqlbucket.utils import integrity_logo, success
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlbucket.exceptions import PassedFieldNotInQuery


def run_integrity(configuration: dict, prefix: str = '', verbose: bool = False):
    pass


class IntegrityCheck:

    def __init__(self, rows: list, query_name: str):
        pass

    def has_passed(self) -> bool:
        pass

    def log_summary(self, query_name: str) -> str:

        pass

    def log_rows(self) -> print:
        pass

    def is_passed_field_missing(self):
        pass

