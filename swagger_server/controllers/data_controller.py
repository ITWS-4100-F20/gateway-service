import connexion
import six

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.models.data_row import DataRow  # noqa: E501
from swagger_server.models.data_schema import DataSchema  # noqa: E501
from swagger_server import util
from swagger_server.utils.database import client


def delete_data(name):  # noqa: E501
    """Delete data of scheme type

     # noqa: E501

    :param id: id of schema
    :type id: 

    :rtype: int
    """

    try:
        data = client["simulation_data"][name]
        amount = data.count()
        if amount > 0:
            data.drop()
            return "{'Rows Affected':" + str(amount) + "}", 200
        else:
            return "Schema does not exist", 400
    except:
        return 'Failed', 400


def get_data(name, amount=None, filters=None):  # noqa: E501
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

    try:
        data = client["simulation_data"][name]
        maxx = data.count()
        if maxx  > 0:
            if(amount is None):
                amount = maxx
            if filters is None:
                filters = {}
            return([DataRow.from_dict(dict(i)) for i in data.find(filters).limit(amount)])
        else:
            return "Schema or data does not exist", 400
    except:
        return 'Failed', 400

def post_add_data(body, name):  # noqa: E501
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

    db = client["simulation_data"]
    if db["Schema"].find_one({"name": name}) is not None:
        coll = db[name]
        coll.insert_many([i.to_dict() for i in body.data])
    else:
        return 'Schema for this data does not exist', 400
    return 'Data Added', 200


def put_add_scheme(body):  # noqa: E501
    """Add data scheme

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    
    if connexion.request.is_json:
        body = DataSchema.from_dict(connexion.request.get_json())  # noqa: E501

    database = client["simulation_data"]
    if database["Schema"].find_one({"name": body.name}) is None:
        newcol = database[body.name]
        schema = database["Schema"]
        schema.insert_one(body.to_dict())
    else:
        return 'Schema NAME Exists', 400
    return 'Schema Added', 200
