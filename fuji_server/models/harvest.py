# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fuji_server.models.base_model_ import Model
from fuji_server import util


class Harvest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, object_identifier: str=None):  # noqa: E501
        """Harvest - a model defined in Swagger

        :param object_identifier: The object_identifier of this Harvest.  # noqa: E501
        :type object_identifier: str
        """
        self.swagger_types = {
            'object_identifier': str
        }

        self.attribute_map = {
            'object_identifier': 'object_identifier'
        }
        self._object_identifier = object_identifier

    @classmethod
    def from_dict(cls, dikt) -> 'Harvest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The harvest of this Harvest.  # noqa: E501
        :rtype: Harvest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def object_identifier(self) -> str:
        """Gets the object_identifier of this Harvest.

        The full identifier of data object that needs to be harvested  # noqa: E501

        :return: The object_identifier of this Harvest.
        :rtype: str
        """
        return self._object_identifier

    @object_identifier.setter
    def object_identifier(self, object_identifier: str):
        """Sets the object_identifier of this Harvest.

        The full identifier of data object that needs to be harvested  # noqa: E501

        :param object_identifier: The object_identifier of this Harvest.
        :type object_identifier: str
        """
        if object_identifier is None:
            raise ValueError('Invalid value for `object_identifier`, must not be `None`')  # noqa: E501

        self._object_identifier = object_identifier
