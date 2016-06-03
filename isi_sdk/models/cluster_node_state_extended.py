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


class ClusterNodeStateExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterNodeStateExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'readonly': 'NodeStateReadonlyExtended',
            'servicelight': 'ClusterNodeStateServicelightExtended',
            'smartfail': 'NodeStateSmartfailExtended'
        }

        self.attribute_map = {
            'readonly': 'readonly',
            'servicelight': 'servicelight',
            'smartfail': 'smartfail'
        }

        self._readonly = None
        self._servicelight = None
        self._smartfail = None

    @property
    def readonly(self):
        """
        Gets the readonly of this ClusterNodeStateExtended.
        Node readonly state.

        :return: The readonly of this ClusterNodeStateExtended.
        :rtype: NodeStateReadonlyExtended
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """
        Sets the readonly of this ClusterNodeStateExtended.
        Node readonly state.

        :param readonly: The readonly of this ClusterNodeStateExtended.
        :type: NodeStateReadonlyExtended
        """
        
        self._readonly = readonly

    @property
    def servicelight(self):
        """
        Gets the servicelight of this ClusterNodeStateExtended.
        Node service light state.

        :return: The servicelight of this ClusterNodeStateExtended.
        :rtype: ClusterNodeStateServicelightExtended
        """
        return self._servicelight

    @servicelight.setter
    def servicelight(self, servicelight):
        """
        Sets the servicelight of this ClusterNodeStateExtended.
        Node service light state.

        :param servicelight: The servicelight of this ClusterNodeStateExtended.
        :type: ClusterNodeStateServicelightExtended
        """
        
        self._servicelight = servicelight

    @property
    def smartfail(self):
        """
        Gets the smartfail of this ClusterNodeStateExtended.
        Node smartfail state.

        :return: The smartfail of this ClusterNodeStateExtended.
        :rtype: NodeStateSmartfailExtended
        """
        return self._smartfail

    @smartfail.setter
    def smartfail(self, smartfail):
        """
        Sets the smartfail of this ClusterNodeStateExtended.
        Node smartfail state.

        :param smartfail: The smartfail of this ClusterNodeStateExtended.
        :type: NodeStateSmartfailExtended
        """
        
        self._smartfail = smartfail

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

