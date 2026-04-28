from sqlbucket.project import Project
from sqlbucket.exceptions import ProjectNotFound, ConnectionNotFound, \
    ReservedVariableNameError
from sqlbucket.cli import load_cli
from pathlib import Path
from distutils.dir_util import copy_tree
import os
from typing import List, Callable


class SQLBucket:

    def __init__(
        self,
        projects_folder: str = 'projects',
        connections: dict = None,
        connection_variables: dict = None,
        env_name: str = None,       # todo: see if we can remove
        environment_variables: dict = None,
        macro_folder: str = None,
        functions_registry: List[Callable] = None
    ):

        pass

    def load_project(self, project_name: str, connection_name: str,
                     variables: dict = None) -> Project:
        """
        Load a project for a given project name and a given connection name.
        :param project_name
        :param connection_name
        :param variables: Typically variables submitted via CLI
        :return: Project instance
        """

        pass

    def create_project(self, project_name: str):
        pass

    def connection_exists(self, connection_name: str) -> bool:
        pass

    def cli(self):
        pass

    def build_context(self, connection_name: str, variables: dict):
        pass

    def register_function(self, func: Callable):
        pass
