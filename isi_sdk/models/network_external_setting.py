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


class NetworkExternalSetting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NetworkExternalSetting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'default_groupnet': 'str',
            'sbr': 'bool',
            'sc_rebalance_delay': 'int',
            'tcp_ports': 'list[int]'
        }

        self.attribute_map = {
            'default_groupnet': 'default_groupnet',
            'sbr': 'sbr',
            'sc_rebalance_delay': 'sc_rebalance_delay',
            'tcp_ports': 'tcp_ports'
        }

        self._default_groupnet = None
        self._sbr = None
        self._sc_rebalance_delay = None
        self._tcp_ports = None

    @property
    def default_groupnet(self):
        """
        Gets the default_groupnet of this NetworkExternalSetting.
        Default client-side DNS settings for non-multitenancy aware programs

        :return: The default_groupnet of this NetworkExternalSetting.
        :rtype: str
        """
        return self._default_groupnet

    @default_groupnet.setter
    def default_groupnet(self, default_groupnet):
        """
        Sets the default_groupnet of this NetworkExternalSetting.
        Default client-side DNS settings for non-multitenancy aware programs

        :param default_groupnet: The default_groupnet of this NetworkExternalSetting.
        :type: str
        """
        
        self._default_groupnet = default_groupnet

    @property
    def sbr(self):
        """
        Gets the sbr of this NetworkExternalSetting.
        Enable or disable Source Based Routing (Defaults to false)

        :return: The sbr of this NetworkExternalSetting.
        :rtype: bool
        """
        return self._sbr

    @sbr.setter
    def sbr(self, sbr):
        """
        Sets the sbr of this NetworkExternalSetting.
        Enable or disable Source Based Routing (Defaults to false)

        :param sbr: The sbr of this NetworkExternalSetting.
        :type: bool
        """
        
        self._sbr = sbr

    @property
    def sc_rebalance_delay(self):
        """
        Gets the sc_rebalance_delay of this NetworkExternalSetting.
        Delay in seconds for IP rebalance.

        :return: The sc_rebalance_delay of this NetworkExternalSetting.
        :rtype: int
        """
        return self._sc_rebalance_delay

    @sc_rebalance_delay.setter
    def sc_rebalance_delay(self, sc_rebalance_delay):
        """
        Sets the sc_rebalance_delay of this NetworkExternalSetting.
        Delay in seconds for IP rebalance.

        :param sc_rebalance_delay: The sc_rebalance_delay of this NetworkExternalSetting.
        :type: int
        """
        
        if not sc_rebalance_delay:
            raise ValueError("Invalid value for `sc_rebalance_delay`, must not be `None`")
        if sc_rebalance_delay > 10.0: 
            raise ValueError("Invalid value for `sc_rebalance_delay`, must be a value less than or equal to `10.0`")
        if sc_rebalance_delay < 0.0: 
            raise ValueError("Invalid value for `sc_rebalance_delay`, must be a value greater than or equal to `0.0`")

        self._sc_rebalance_delay = sc_rebalance_delay

    @property
    def tcp_ports(self):
        """
        Gets the tcp_ports of this NetworkExternalSetting.
        List of client TCP ports.

        :return: The tcp_ports of this NetworkExternalSetting.
        :rtype: list[int]
        """
        return self._tcp_ports

    @tcp_ports.setter
    def tcp_ports(self, tcp_ports):
        """
        Sets the tcp_ports of this NetworkExternalSetting.
        List of client TCP ports.

        :param tcp_ports: The tcp_ports of this NetworkExternalSetting.
        :type: list[int]
        """
        
        self._tcp_ports = tcp_ports

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

