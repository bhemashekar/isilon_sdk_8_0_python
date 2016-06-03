# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class ClusterIdentityLogonExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterIdentityLogonExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'motd': 'str',
            'motd_header': 'str'
        }

        self.attribute_map = {
            'motd': 'motd',
            'motd_header': 'motd_header'
        }

        self._motd = None
        self._motd_header = None

    @property
    def motd(self):
        """
        Gets the motd of this ClusterIdentityLogonExtended.
        The message of the day.

        :return: The motd of this ClusterIdentityLogonExtended.
        :rtype: str
        """
        return self._motd

    @motd.setter
    def motd(self, motd):
        """
        Sets the motd of this ClusterIdentityLogonExtended.
        The message of the day.

        :param motd: The motd of this ClusterIdentityLogonExtended.
        :type: str
        """
        
        self._motd = motd

    @property
    def motd_header(self):
        """
        Gets the motd_header of this ClusterIdentityLogonExtended.
        The header to the message of the day.

        :return: The motd_header of this ClusterIdentityLogonExtended.
        :rtype: str
        """
        return self._motd_header

    @motd_header.setter
    def motd_header(self, motd_header):
        """
        Sets the motd_header of this ClusterIdentityLogonExtended.
        The header to the message of the day.

        :param motd_header: The motd_header of this ClusterIdentityLogonExtended.
        :type: str
        """
        
        self._motd_header = motd_header

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

