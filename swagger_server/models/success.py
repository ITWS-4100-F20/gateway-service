# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Success(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: float=None, message: str=None):  # noqa: E501
        """Success - a model defined in Swagger

        :param code: The code of this Success.  # noqa: E501
        :type code: float
        :param message: The message of this Success.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'code': float,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }
        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'Success':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Success of this Success.  # noqa: E501
        :rtype: Success
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> float:
        """Gets the code of this Success.


        :return: The code of this Success.
        :rtype: float
        """
        return self._code

    @code.setter
    def code(self, code: float):
        """Sets the code of this Success.


        :param code: The code of this Success.
        :type code: float
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this Success.


        :return: The message of this Success.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this Success.


        :param message: The message of this Success.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
