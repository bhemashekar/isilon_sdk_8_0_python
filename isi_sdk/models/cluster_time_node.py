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


class ClusterTimeNode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterTimeNode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'error': 'str',
            'id': 'int',
            'lnn': 'int',
            'status': 'int',
            'time': 'int'
        }

        self.attribute_map = {
            'error': 'error',
            'id': 'id',
            'lnn': 'lnn',
            'status': 'status',
            'time': 'time'
        }

        self._error = None
        self._id = None
        self._lnn = None
        self._status = None
        self._time = None

    @property
    def error(self):
        """
        Gets the error of this ClusterTimeNode.
        Error message, if the HTTP status returned from this node was not 200.

        :return: The error of this ClusterTimeNode.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ClusterTimeNode.
        Error message, if the HTTP status returned from this node was not 200.

        :param error: The error of this ClusterTimeNode.
        :type: str
        """
        
        self._error = error

    @property
    def id(self):
        """
        Gets the id of this ClusterTimeNode.
        Node ID of the node reporting this information.

        :return: The id of this ClusterTimeNode.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClusterTimeNode.
        Node ID of the node reporting this information.

        :param id: The id of this ClusterTimeNode.
        :type: int
        """
        
        if id is not None  and id > 4.294967295E9:
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `4.294967295E9`")
        if id is not None and id < 0.0:
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0.0`")

        self._id = id

    @property
    def lnn(self):
        """
        Gets the lnn of this ClusterTimeNode.
        Logical node number of the node reporting this information.

        :return: The lnn of this ClusterTimeNode.
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """
        Sets the lnn of this ClusterTimeNode.
        Logical node number of the node reporting this information.

        :param lnn: The lnn of this ClusterTimeNode.
        :type: int
        """
        
        if lnn is not None  and lnn > 4.294967295E9:
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `4.294967295E9`")
        if lnn is not None and lnn < 0.0:
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `0.0`")

        self._lnn = lnn

    @property
    def status(self):
        """
        Gets the status of this ClusterTimeNode.
        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.

        :return: The status of this ClusterTimeNode.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ClusterTimeNode.
        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.

        :param status: The status of this ClusterTimeNode.
        :type: int
        """
        
        if status is not None  and status > 4.294967295E9:
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4.294967295E9`")
        if status is not None and status < 0.0:
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0.0`")

        self._status = status

    @property
    def time(self):
        """
        Gets the time of this ClusterTimeNode.
        The current time on the cluster as a UNIX epoch (seconds since 1/1/1970), as reported by this node.

        :return: The time of this ClusterTimeNode.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this ClusterTimeNode.
        The current time on the cluster as a UNIX epoch (seconds since 1/1/1970), as reported by this node.

        :param time: The time of this ClusterTimeNode.
        :type: int
        """
        
        if time is not None  and time > 9.223372036854776E18:
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `9.223372036854776E18`")
        if time is not None and time < -9.223372036854776E18:
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `-9.223372036854776E18`")

        self._time = time

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

