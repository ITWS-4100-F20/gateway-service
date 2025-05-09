# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.data_row import DataRow  # noqa: F401,E501
from swagger_server import util


class Data(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, data: List[DataRow]=None):  # noqa: E501
        """Data - a model defined in Swagger

        :param data: The data of this Data.  # noqa: E501
        :type data: List[DataRow]
        """
        self.swagger_types = {
            'data': List[DataRow]
        }

        self.attribute_map = {
            'data': 'data'
        }
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Data of this Data.  # noqa: E501
        :rtype: Data
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self) -> List[DataRow]:
        """Gets the data of this Data.


        :return: The data of this Data.
        :rtype: List[DataRow]
        """
        return self._data

    @data.setter
    def data(self, data: List[DataRow]):
        """Sets the data of this Data.


        :param data: The data of this Data.
        :type data: List[DataRow]
        """

        self._data = data
