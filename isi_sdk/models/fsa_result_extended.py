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


class FsaResultExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FsaResultExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pinned': 'bool',
            'begin_time': 'int',
            'content_path': 'str',
            'delete_link': 'str',
            'end_time': 'int',
            'fsa_state': 'str',
            'id': 'int',
            'job_state': 'list[str]',
            'properties_link': 'str',
            'size': 'int',
            'version': 'int'
        }

        self.attribute_map = {
            'pinned': 'pinned',
            'begin_time': 'begin_time',
            'content_path': 'content_path',
            'delete_link': 'delete_link',
            'end_time': 'end_time',
            'fsa_state': 'fsa_state',
            'id': 'id',
            'job_state': 'job_state',
            'properties_link': 'properties_link',
            'size': 'size',
            'version': 'version'
        }

        self._pinned = None
        self._begin_time = None
        self._content_path = None
        self._delete_link = None
        self._end_time = None
        self._fsa_state = None
        self._id = None
        self._job_state = None
        self._properties_link = None
        self._size = None
        self._version = None

    @property
    def pinned(self):
        """
        Gets the pinned of this FsaResultExtended.
        True if the result is pinned to prevent automatic removal.

        :return: The pinned of this FsaResultExtended.
        :rtype: bool
        """
        return self._pinned

    @pinned.setter
    def pinned(self, pinned):
        """
        Sets the pinned of this FsaResultExtended.
        True if the result is pinned to prevent automatic removal.

        :param pinned: The pinned of this FsaResultExtended.
        :type: bool
        """
        
        self._pinned = pinned

    @property
    def begin_time(self):
        """
        Gets the begin_time of this FsaResultExtended.
        Unix Epoch time of start of results collection job.

        :return: The begin_time of this FsaResultExtended.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """
        Sets the begin_time of this FsaResultExtended.
        Unix Epoch time of start of results collection job.

        :param begin_time: The begin_time of this FsaResultExtended.
        :type: int
        """
        
        self._begin_time = begin_time

    @property
    def content_path(self):
        """
        Gets the content_path of this FsaResultExtended.
        Path to results database.

        :return: The content_path of this FsaResultExtended.
        :rtype: str
        """
        return self._content_path

    @content_path.setter
    def content_path(self, content_path):
        """
        Sets the content_path of this FsaResultExtended.
        Path to results database.

        :param content_path: The content_path of this FsaResultExtended.
        :type: str
        """
        
        self._content_path = content_path

    @property
    def delete_link(self):
        """
        Gets the delete_link of this FsaResultExtended.
        Resource to call with DELETE to remove results..

        :return: The delete_link of this FsaResultExtended.
        :rtype: str
        """
        return self._delete_link

    @delete_link.setter
    def delete_link(self, delete_link):
        """
        Sets the delete_link of this FsaResultExtended.
        Resource to call with DELETE to remove results..

        :param delete_link: The delete_link of this FsaResultExtended.
        :type: str
        """
        
        self._delete_link = delete_link

    @property
    def end_time(self):
        """
        Gets the end_time of this FsaResultExtended.
        Unix Epoch time of end of results collection job.

        :return: The end_time of this FsaResultExtended.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this FsaResultExtended.
        Unix Epoch time of end of results collection job.

        :param end_time: The end_time of this FsaResultExtended.
        :type: int
        """
        
        self._end_time = end_time

    @property
    def fsa_state(self):
        """
        Gets the fsa_state of this FsaResultExtended.
        State of the result set.

        :return: The fsa_state of this FsaResultExtended.
        :rtype: str
        """
        return self._fsa_state

    @fsa_state.setter
    def fsa_state(self, fsa_state):
        """
        Sets the fsa_state of this FsaResultExtended.
        State of the result set.

        :param fsa_state: The fsa_state of this FsaResultExtended.
        :type: str
        """
        allowed_values = ["unknown", "work", "reduce", "publish"]
        if fsa_state not in allowed_values:
            raise ValueError(
                "Invalid value for `fsa_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._fsa_state = fsa_state

    @property
    def id(self):
        """
        Gets the id of this FsaResultExtended.
        The system generated result set ID.

        :return: The id of this FsaResultExtended.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FsaResultExtended.
        The system generated result set ID.

        :param id: The id of this FsaResultExtended.
        :type: int
        """
        
        self._id = id

    @property
    def job_state(self):
        """
        Gets the job_state of this FsaResultExtended.
        State information about the FSA Job.

        :return: The job_state of this FsaResultExtended.
        :rtype: list[str]
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """
        Sets the job_state of this FsaResultExtended.
        State information about the FSA Job.

        :param job_state: The job_state of this FsaResultExtended.
        :type: list[str]
        """
        
        self._job_state = job_state

    @property
    def properties_link(self):
        """
        Gets the properties_link of this FsaResultExtended.
        Resource to call to get result properties.

        :return: The properties_link of this FsaResultExtended.
        :rtype: str
        """
        return self._properties_link

    @properties_link.setter
    def properties_link(self, properties_link):
        """
        Sets the properties_link of this FsaResultExtended.
        Resource to call to get result properties.

        :param properties_link: The properties_link of this FsaResultExtended.
        :type: str
        """
        
        self._properties_link = properties_link

    @property
    def size(self):
        """
        Gets the size of this FsaResultExtended.
        Size of the result set database in bytes.

        :return: The size of this FsaResultExtended.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this FsaResultExtended.
        Size of the result set database in bytes.

        :param size: The size of this FsaResultExtended.
        :type: int
        """
        
        self._size = size

    @property
    def version(self):
        """
        Gets the version of this FsaResultExtended.
        FSA version used to create result set.

        :return: The version of this FsaResultExtended.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this FsaResultExtended.
        FSA version used to create result set.

        :param version: The version of this FsaResultExtended.
        :type: int
        """
        
        self._version = version

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

