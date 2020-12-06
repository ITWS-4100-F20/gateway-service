import connexion
import six
import json

from swagger_server import util

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.models.data_row import DataRow  # noqa: E501
from swagger_server.models.data_schema import DataSchema  # noqa: E501
from swagger_server import util
from swagger_server.utils.database import client

def get_scenario():  # noqa: E501
    """Lists scenarios with no id. With id it returns data for scenario

     # noqa: E501


    :rtype: None
    """

    scenarios = [i for i in client["simulation_data"]["scenarios"].find({}, { "_id": False })] 
    print(scenarios)
    return scenarios


def post_scenario():  # noqa: E501
    """Creates new scenario

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
