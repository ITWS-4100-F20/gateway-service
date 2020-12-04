import connexion
import six
import json

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.models.data_row import DataRow  # noqa: E501
from swagger_server.models.data_schema import DataSchema  # noqa: E501
from swagger_server import util
from swagger_server.utils.database import client
from swagger_server.controllers.data_controller import post_add_data

def get_data_schemes():  # noqa: E501
    """Lists all data shemes

     # noqa: E501


    :rtype: List[DataSchema]
    """
    schema = [DataSchema.from_dict(dict(i)) for i in client["simulation_data"]["schema"].find()]
    return schema

def data_maker(body):
    import sys
    data = [i.strip().split(',') for i in str(body).strip().split('\n')]
    columns = data[0]
    types = data[1]
    data = data[2:]
    rows = []
    dataTemp = {"data": ""}
    rowTemp2 = {"fields": ""}
    itemTemp2 = {"datatype": "","field": "","value": ""}
    for row in data:
        items = []
        for col in range(0, len(columns)):
            itemTemp = itemTemp2.copy()
            itemTemp["datatype"] = types[col]
            itemTemp["field"] = columns[col]
            itemTemp["value"] = row[col]
            items.append(itemTemp)
        rowTemp = rowTemp2.copy()
        rowTemp["fields"] = items
        rows.append(rowTemp)
    dataTemp["data"] = rows
    return dataTemp    


def post_schema_data(body, name):
    """Add data of scheme type

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: id of schema
    :type id: 

    :rtype: None
    """

    data = data_maker(body.decode('ascii'))
    return post_add_data(Data.from_dict(data), name)
