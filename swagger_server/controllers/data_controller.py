import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.models.data_row import DataRow  # noqa: E501
from swagger_server.models.data_schema import DataSchema  # noqa: E501
from swagger_server import util
from swagger_server.utils.database import client as db


def delete_data(id):  # noqa: E501
    """Delete data of scheme type

     # noqa: E501

    :param id: id of schema
    :type id: 

    :rtype: int
    """
    return 'do some magic!'


def get_data(id, amount=None, filters=None):  # noqa: E501
    """Get data of scheme type

     # noqa: E501

    :param id: id of schema
    :type id: 
    :param amount: amount of data
    :type amount: int
    :param filters: column specific filters (..:columnname,value)
    :type filters: List[str]

    :rtype: List[DataRow]
    """
    return 'do some magic!'


def get_data_schemes():  # noqa: E501
    """Lists all data shemes

     # noqa: E501


    :rtype: List[DataSchema]
    """
    return 'do some magic!'


def post_add_data(body, id):  # noqa: E501
    """Add data of scheme type

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: id of schema
    :type id: 

    :rtype: None
    """
    if connexion.request.is_json:
        body = Data.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_add_scheme(body):  # noqa: E501
    """Add data scheme

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    
    if connexion.request.is_json:
        body = DataSchema.from_dict(connexion.request.get_json())  # noqa: E501

    database = db["simulation_data"]
    if not body.id in database.list_collection_names():
        newcol = database[body.id]
        schema = database["schema"]
        schema.insert_one(body.to_dict())
    else:
        return 'Schema Exists', 400
    return 'Worked'
