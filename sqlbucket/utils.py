import logging
import sys
from datetime import datetime, timedelta


logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] : %(message)s'
)
logger = logging.getLogger()


def n_days_ago(n):
    pass


def cli_variables_parser(cli_variables: list = None) -> dict:
    pass


sqlbucket_logo = r"""

           _____ ____    __    ____             __        __ 
          / ___// __ \  / /   / __ )__  _______/ /_____  / /_
          \__ \/ / / / / /   / __  / / / / ___/ //_/ _ \/ __/
         ___/ / /_/ / / /___/ /_/ / /_/ / /__/ ,< /  __/ /_  
        /____/\___\_\/_____/_____/\__,_/\___/_/|_|\___/\__/  

        """


integrity_logo = r"""

            ____      __                  _ __       
           /  _/___  / /____  ____ ______(_) /___  __
           / // __ \/ __/ _ \/ __ `/ ___/ / __/ / / /
         _/ // / / / /_/  __/ /_/ / /  / / /_/ /_/ / 
        /___/_/ /_/\__/\___/\__, /_/  /_/\__/\__, /  
                           /____/           /____/   

        """

success = r"""
            
            ___|
                                                   
         \___ \   |   |   __|   __|   _ \   __|   __| 
               |  |   |  (     (      __/ \__ \ \__ \ 
         _____/  \__,_| \___| \___| \___| ____/ ____/ 
                                          
        """
