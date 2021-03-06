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


class NodeStatusNodePowersuppliesSupply(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodeStatusNodePowersuppliesSupply - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'chassis': 'int',
            'firmware': 'str',
            'good': 'str',
            'id': 'int',
            'name': 'str',
            'status': 'str',
            'type': 'str'
        }

        self.attribute_map = {
            'chassis': 'chassis',
            'firmware': 'firmware',
            'good': 'good',
            'id': 'id',
            'name': 'name',
            'status': 'status',
            'type': 'type'
        }

        self._chassis = None
        self._firmware = None
        self._good = None
        self._id = None
        self._name = None
        self._status = None
        self._type = None

    @property
    def chassis(self):
        """
        Gets the chassis of this NodeStatusNodePowersuppliesSupply.
        Which node chassis is this power supply in.

        :return: The chassis of this NodeStatusNodePowersuppliesSupply.
        :rtype: int
        """
        return self._chassis

    @chassis.setter
    def chassis(self, chassis):
        """
        Sets the chassis of this NodeStatusNodePowersuppliesSupply.
        Which node chassis is this power supply in.

        :param chassis: The chassis of this NodeStatusNodePowersuppliesSupply.
        :type: int
        """
        
        self._chassis = chassis

    @property
    def firmware(self):
        """
        Gets the firmware of this NodeStatusNodePowersuppliesSupply.
        The current firmware revision of this power supply.

        :return: The firmware of this NodeStatusNodePowersuppliesSupply.
        :rtype: str
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this NodeStatusNodePowersuppliesSupply.
        The current firmware revision of this power supply.

        :param firmware: The firmware of this NodeStatusNodePowersuppliesSupply.
        :type: str
        """
        
        self._firmware = firmware

    @property
    def good(self):
        """
        Gets the good of this NodeStatusNodePowersuppliesSupply.
        Is this power supply in a failure state.

        :return: The good of this NodeStatusNodePowersuppliesSupply.
        :rtype: str
        """
        return self._good

    @good.setter
    def good(self, good):
        """
        Sets the good of this NodeStatusNodePowersuppliesSupply.
        Is this power supply in a failure state.

        :param good: The good of this NodeStatusNodePowersuppliesSupply.
        :type: str
        """
        
        self._good = good

    @property
    def id(self):
        """
        Gets the id of this NodeStatusNodePowersuppliesSupply.
        Identifying index for this power supply.

        :return: The id of this NodeStatusNodePowersuppliesSupply.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NodeStatusNodePowersuppliesSupply.
        Identifying index for this power supply.

        :param id: The id of this NodeStatusNodePowersuppliesSupply.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this NodeStatusNodePowersuppliesSupply.
        Complete identifying string for this power supply.

        :return: The name of this NodeStatusNodePowersuppliesSupply.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this NodeStatusNodePowersuppliesSupply.
        Complete identifying string for this power supply.

        :param name: The name of this NodeStatusNodePowersuppliesSupply.
        :type: str
        """
        
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this NodeStatusNodePowersuppliesSupply.
        A descriptive status string for this power supply.

        :return: The status of this NodeStatusNodePowersuppliesSupply.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NodeStatusNodePowersuppliesSupply.
        A descriptive status string for this power supply.

        :param status: The status of this NodeStatusNodePowersuppliesSupply.
        :type: str
        """
        
        self._status = status

    @property
    def type(self):
        """
        Gets the type of this NodeStatusNodePowersuppliesSupply.
        The type of this power supply.

        :return: The type of this NodeStatusNodePowersuppliesSupply.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this NodeStatusNodePowersuppliesSupply.
        The type of this power supply.

        :param type: The type of this NodeStatusNodePowersuppliesSupply.
        :type: str
        """
        
        self._type = type

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

