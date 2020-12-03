import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.models.data_row import DataRow  # noqa: E501
from swagger_server.models.data_schema import DataSchema  # noqa: E501
from swagger_server import util
from swagger_server.utils.database import client

def get_data_schemes():  # noqa: E501
    """Lists all data shemes

     # noqa: E501


    :rtype: List[DataSchema]
    """
    schema = [DataSchema.from_dict(dict(i)) for i in client["simulation_data"]["schema"].find()]
    return schema