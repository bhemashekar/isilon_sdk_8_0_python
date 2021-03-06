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


class HardwareFcports(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        HardwareFcports - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'port': 'str',
            'rate': 'str',
            'state': 'str',
            'topology': 'str',
            'wwnn': 'str',
            'wwpn': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'port': 'port',
            'rate': 'rate',
            'state': 'state',
            'topology': 'topology',
            'wwnn': 'wwnn',
            'wwpn': 'wwpn'
        }

        self._id = None
        self._port = None
        self._rate = None
        self._state = None
        self._topology = None
        self._wwnn = None
        self._wwpn = None

    @property
    def id(self):
        """
        Gets the id of this HardwareFcports.
        The unique display id

        :return: The id of this HardwareFcports.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this HardwareFcports.
        The unique display id

        :param id: The id of this HardwareFcports.
        :type: str
        """
        
        self._id = id

    @property
    def port(self):
        """
        Gets the port of this HardwareFcports.
        Port ID

        :return: The port of this HardwareFcports.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this HardwareFcports.
        Port ID

        :param port: The port of this HardwareFcports.
        :type: str
        """
        
        self._port = port

    @property
    def rate(self):
        """
        Gets the rate of this HardwareFcports.


        :return: The rate of this HardwareFcports.
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this HardwareFcports.


        :param rate: The rate of this HardwareFcports.
        :type: str
        """
        allowed_values = ["auto", "1", "2", "4", "8"]
        if rate not in allowed_values:
            raise ValueError(
                "Invalid value for `rate`, must be one of {0}"
                .format(allowed_values)
            )

        self._rate = rate

    @property
    def state(self):
        """
        Gets the state of this HardwareFcports.
        State of the port

        :return: The state of this HardwareFcports.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this HardwareFcports.
        State of the port

        :param state: The state of this HardwareFcports.
        :type: str
        """
        allowed_values = ["enable", "disable"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )

        self._state = state

    @property
    def topology(self):
        """
        Gets the topology of this HardwareFcports.


        :return: The topology of this HardwareFcports.
        :rtype: str
        """
        return self._topology

    @topology.setter
    def topology(self, topology):
        """
        Sets the topology of this HardwareFcports.


        :param topology: The topology of this HardwareFcports.
        :type: str
        """
        allowed_values = ["auto", "ptp", "loop"]
        if topology not in allowed_values:
            raise ValueError(
                "Invalid value for `topology`, must be one of {0}"
                .format(allowed_values)
            )

        self._topology = topology

    @property
    def wwnn(self):
        """
        Gets the wwnn of this HardwareFcports.
        World wide node name of the port

        :return: The wwnn of this HardwareFcports.
        :rtype: str
        """
        return self._wwnn

    @wwnn.setter
    def wwnn(self, wwnn):
        """
        Sets the wwnn of this HardwareFcports.
        World wide node name of the port

        :param wwnn: The wwnn of this HardwareFcports.
        :type: str
        """
        
        self._wwnn = wwnn

    @property
    def wwpn(self):
        """
        Gets the wwpn of this HardwareFcports.
        World wide port name of the port

        :return: The wwpn of this HardwareFcports.
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """
        Sets the wwpn of this HardwareFcports.
        World wide port name of the port

        :param wwpn: The wwpn of this HardwareFcports.
        :type: str
        """
        
        self._wwpn = wwpn

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

