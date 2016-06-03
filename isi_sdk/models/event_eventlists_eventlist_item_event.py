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


class EventEventlistsEventlistItemEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EventEventlistsEventlistItemEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'devid': 'int',
            'ended': 'float',
            'event_id': 'int',
            'id': 'str',
            'message': 'str',
            'severity': 'str',
            'specifier': 'Empty',
            'time': 'int',
            'value': 'float'
        }

        self.attribute_map = {
            'devid': 'devid',
            'ended': 'ended',
            'event_id': 'event_id',
            'id': 'id',
            'message': 'message',
            'severity': 'severity',
            'specifier': 'specifier',
            'time': 'time',
            'value': 'value'
        }

        self._devid = None
        self._ended = None
        self._event_id = None
        self._id = None
        self._message = None
        self._severity = None
        self._specifier = None
        self._time = None
        self._value = None

    @property
    def devid(self):
        """
        Gets the devid of this EventEventlistsEventlistItemEvent.
        The lnn of the node if it is still part of the cluster otherwise None.

        :return: The devid of this EventEventlistsEventlistItemEvent.
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """
        Sets the devid of this EventEventlistsEventlistItemEvent.
        The lnn of the node if it is still part of the cluster otherwise None.

        :param devid: The devid of this EventEventlistsEventlistItemEvent.
        :type: int
        """
        
        self._devid = devid

    @property
    def ended(self):
        """
        Gets the ended of this EventEventlistsEventlistItemEvent.
        Time event was ended (eventgroup resolved)

        :return: The ended of this EventEventlistsEventlistItemEvent.
        :rtype: float
        """
        return self._ended

    @ended.setter
    def ended(self, ended):
        """
        Sets the ended of this EventEventlistsEventlistItemEvent.
        Time event was ended (eventgroup resolved)

        :param ended: The ended of this EventEventlistsEventlistItemEvent.
        :type: float
        """
        
        self._ended = ended

    @property
    def event_id(self):
        """
        Gets the event_id of this EventEventlistsEventlistItemEvent.
        Integer identifier of the event type

        :return: The event_id of this EventEventlistsEventlistItemEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this EventEventlistsEventlistItemEvent.
        Integer identifier of the event type

        :param event_id: The event_id of this EventEventlistsEventlistItemEvent.
        :type: int
        """
        
        self._event_id = event_id

    @property
    def id(self):
        """
        Gets the id of this EventEventlistsEventlistItemEvent.
        Unique identifier of event occurrence.

        :return: The id of this EventEventlistsEventlistItemEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EventEventlistsEventlistItemEvent.
        Unique identifier of event occurrence.

        :param id: The id of this EventEventlistsEventlistItemEvent.
        :type: str
        """
        
        self._id = id

    @property
    def message(self):
        """
        Gets the message of this EventEventlistsEventlistItemEvent.
        Human readable description

        :return: The message of this EventEventlistsEventlistItemEvent.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this EventEventlistsEventlistItemEvent.
        Human readable description

        :param message: The message of this EventEventlistsEventlistItemEvent.
        :type: str
        """
        
        self._message = message

    @property
    def severity(self):
        """
        Gets the severity of this EventEventlistsEventlistItemEvent.
        Severity of event occurrence.

        :return: The severity of this EventEventlistsEventlistItemEvent.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """
        Sets the severity of this EventEventlistsEventlistItemEvent.
        Severity of event occurrence.

        :param severity: The severity of this EventEventlistsEventlistItemEvent.
        :type: str
        """
        allowed_values = ["information", "warning", "critical", "emergency"]
        if severity is not None and severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity`, must be one of {0}"
                .format(allowed_values)
            )

        self._severity = severity

    @property
    def specifier(self):
        """
        Gets the specifier of this EventEventlistsEventlistItemEvent.
        A collection of parameters defined per event.

        :return: The specifier of this EventEventlistsEventlistItemEvent.
        :rtype: Empty
        """
        return self._specifier

    @specifier.setter
    def specifier(self, specifier):
        """
        Sets the specifier of this EventEventlistsEventlistItemEvent.
        A collection of parameters defined per event.

        :param specifier: The specifier of this EventEventlistsEventlistItemEvent.
        :type: Empty
        """
        
        self._specifier = specifier

    @property
    def time(self):
        """
        Gets the time of this EventEventlistsEventlistItemEvent.
        Time event was detected as UNIX timestamp.

        :return: The time of this EventEventlistsEventlistItemEvent.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """
        Sets the time of this EventEventlistsEventlistItemEvent.
        Time event was detected as UNIX timestamp.

        :param time: The time of this EventEventlistsEventlistItemEvent.
        :type: int
        """
        
        self._time = time

    @property
    def value(self):
        """
        Gets the value of this EventEventlistsEventlistItemEvent.
        Value of measurement associated with this event.

        :return: The value of this EventEventlistsEventlistItemEvent.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this EventEventlistsEventlistItemEvent.
        Value of measurement associated with this event.

        :param value: The value of this EventEventlistsEventlistItemEvent.
        :type: float
        """
        
        self._value = value

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

