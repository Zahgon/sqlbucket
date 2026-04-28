from sqlbucket.exceptions import GroupNotFound, OrderNotInRightFormat
from sqlbucket.runners import ProjectRunner
from sqlbucket.integrity import run_integrity
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from typing import Optional
import yaml


class Project:

    def __init__(
        self,
        project_path: str,
        connection_url: str,
        context: dict = None,
        macros_path: str = None
    ):

        pass

    def configure(self, group: str = None) -> dict:
        # Setting up the jinja environment
        pass

    def configure_integrity(self) -> dict:
        # Setting up the jinja environment
        pass

    def send_msg(run_func):

        pass

    @send_msg
    def run(self, group: str = None, from_step: int = 1, to_step: int = None,
            verbose: bool = False, isolation_level: str = None) -> None:
        pass

    def render(self, group: str = None, from_step: int = 1,
               to_step: int = None) -> None:
        pass

    def run_integrity(self, prefix: str = '', verbose: bool = False):
        pass

    def get_project_config(self) -> dict:
        pass

    def get_connection_query(self) -> Optional[str]:
        """
        We create the jinja env from scratch again from the queries folder.
        This is done in case we run the integrity, which will need the
        connection script too. Not really clean, as we create the same
        environment twice.
        :return: the connection query if any.
        """

        pass

    def create_jinja_env(self, folder: str) -> Environment:
        pass


class ContextMerger:
    """
    Class to help merging 2 variables contexts. Original context is the one
    submitted when loading a project. It must be merged with the one found in
    config.

    In case of duplicate keys between the 2 context, we only keep one. The
    context that has priority depends on the variable types.

    Environment and connection variables from the config.yaml of a project will
    overwrite the key/value matching pairs of the one submitted by SQLBucket.

    For project variables, this is opposite, we give priority to the ones submitted
    by the SQLBucket, typically the one submitted in Python or via CLI. The
    logic behind it is that we prefer to give priority to the more dynamic
    approach.

    """
    def __init__(self, context: dict, context_from_config: dict):
        """
        :param context: Context send to project by SQLBucket object.
        :param context_from_config: Context found in config.yaml of a project.
        """
        pass

    def overwrite_environment_variables(self):
        pass

    def overwrite_connection_variables(self):
        pass

    def overwrite_project_variables(self):
        pass

    def merge(self):
        pass
