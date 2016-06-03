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


class AuthAccessAccessItemUser(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthAccessAccessItemUser - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'type': 'str',
            'uid': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'type': 'type',
            'uid': 'uid'
        }

        self._id = None
        self._name = None
        self._type = None
        self._uid = None

    @property
    def id(self):
        """
        Gets the id of this AuthAccessAccessItemUser.
        Specifies the serialized form of the persona, which can be 'UID:0', 'USER:name', 'GID:0', 'GROUP:wheel', or 'SID:S-1-1'.

        :return: The id of this AuthAccessAccessItemUser.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthAccessAccessItemUser.
        Specifies the serialized form of the persona, which can be 'UID:0', 'USER:name', 'GID:0', 'GROUP:wheel', or 'SID:S-1-1'.

        :param id: The id of this AuthAccessAccessItemUser.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AuthAccessAccessItemUser.
        Specifies the persona name, which must be combined with a type.

        :return: The name of this AuthAccessAccessItemUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuthAccessAccessItemUser.
        Specifies the persona name, which must be combined with a type.

        :param name: The name of this AuthAccessAccessItemUser.
        :type: str
        """
        
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this AuthAccessAccessItemUser.
        Specifies the type, which must be combined with a name.

        :return: The type of this AuthAccessAccessItemUser.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AuthAccessAccessItemUser.
        Specifies the type, which must be combined with a name.

        :param type: The type of this AuthAccessAccessItemUser.
        :type: str
        """
        allowed_values = ["user", "group", "wellknown"]
        if type is not None and type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )

        self._type = type

    @property
    def uid(self):
        """
        Gets the uid of this AuthAccessAccessItemUser.
        Specifies the uid of the user.

        :return: The uid of this AuthAccessAccessItemUser.
        :rtype: int
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """
        Sets the uid of this AuthAccessAccessItemUser.
        Specifies the uid of the user.

        :param uid: The uid of this AuthAccessAccessItemUser.
        :type: int
        """
        
        self._uid = uid

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

