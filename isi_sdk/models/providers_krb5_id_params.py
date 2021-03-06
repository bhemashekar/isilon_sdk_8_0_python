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


class ProvidersKrb5IdParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProvidersKrb5IdParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'keytab_entries': 'list[ProvidersKrb5IdParamsKeytabEntry]',
            'keytab_file': 'str',
            'manual_keying': 'bool',
            'name': 'str',
            'password': 'str',
            'realm': 'str',
            'status': 'str',
            'user': 'str'
        }

        self.attribute_map = {
            'keytab_entries': 'keytab_entries',
            'keytab_file': 'keytab_file',
            'manual_keying': 'manual_keying',
            'name': 'name',
            'password': 'password',
            'realm': 'realm',
            'status': 'status',
            'user': 'user'
        }

        self._keytab_entries = None
        self._keytab_file = None
        self._manual_keying = None
        self._name = None
        self._password = None
        self._realm = None
        self._status = None
        self._user = None

    @property
    def keytab_entries(self):
        """
        Gets the keytab_entries of this ProvidersKrb5IdParams.
        Specifies the key information for the Kerberos SPNs.

        :return: The keytab_entries of this ProvidersKrb5IdParams.
        :rtype: list[ProvidersKrb5IdParamsKeytabEntry]
        """
        return self._keytab_entries

    @keytab_entries.setter
    def keytab_entries(self, keytab_entries):
        """
        Sets the keytab_entries of this ProvidersKrb5IdParams.
        Specifies the key information for the Kerberos SPNs.

        :param keytab_entries: The keytab_entries of this ProvidersKrb5IdParams.
        :type: list[ProvidersKrb5IdParamsKeytabEntry]
        """
        
        self._keytab_entries = keytab_entries

    @property
    def keytab_file(self):
        """
        Gets the keytab_file of this ProvidersKrb5IdParams.
        Specifies the path to a keytab file to import.

        :return: The keytab_file of this ProvidersKrb5IdParams.
        :rtype: str
        """
        return self._keytab_file

    @keytab_file.setter
    def keytab_file(self, keytab_file):
        """
        Sets the keytab_file of this ProvidersKrb5IdParams.
        Specifies the path to a keytab file to import.

        :param keytab_file: The keytab_file of this ProvidersKrb5IdParams.
        :type: str
        """
        
        self._keytab_file = keytab_file

    @property
    def manual_keying(self):
        """
        Gets the manual_keying of this ProvidersKrb5IdParams.
        If true, keys are managed manually. If false, keys are managed through kadmin.

        :return: The manual_keying of this ProvidersKrb5IdParams.
        :rtype: bool
        """
        return self._manual_keying

    @manual_keying.setter
    def manual_keying(self, manual_keying):
        """
        Sets the manual_keying of this ProvidersKrb5IdParams.
        If true, keys are managed manually. If false, keys are managed through kadmin.

        :param manual_keying: The manual_keying of this ProvidersKrb5IdParams.
        :type: bool
        """
        
        self._manual_keying = manual_keying

    @property
    def name(self):
        """
        Gets the name of this ProvidersKrb5IdParams.
        Specifies the Kerberos provider name.

        :return: The name of this ProvidersKrb5IdParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProvidersKrb5IdParams.
        Specifies the Kerberos provider name.

        :param name: The name of this ProvidersKrb5IdParams.
        :type: str
        """
        
        self._name = name

    @property
    def password(self):
        """
        Gets the password of this ProvidersKrb5IdParams.
        Specifies the Kerberos provider password.

        :return: The password of this ProvidersKrb5IdParams.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this ProvidersKrb5IdParams.
        Specifies the Kerberos provider password.

        :param password: The password of this ProvidersKrb5IdParams.
        :type: str
        """
        
        self._password = password

    @property
    def realm(self):
        """
        Gets the realm of this ProvidersKrb5IdParams.
        Specifies the name of realm.

        :return: The realm of this ProvidersKrb5IdParams.
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """
        Sets the realm of this ProvidersKrb5IdParams.
        Specifies the name of realm.

        :param realm: The realm of this ProvidersKrb5IdParams.
        :type: str
        """
        
        self._realm = realm

    @property
    def status(self):
        """
        Gets the status of this ProvidersKrb5IdParams.
        Specifies the status of the provider.

        :return: The status of this ProvidersKrb5IdParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProvidersKrb5IdParams.
        Specifies the status of the provider.

        :param status: The status of this ProvidersKrb5IdParams.
        :type: str
        """
        
        self._status = status

    @property
    def user(self):
        """
        Gets the user of this ProvidersKrb5IdParams.
        Specifies the name of the user that performs kadmin tasks.

        :return: The user of this ProvidersKrb5IdParams.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this ProvidersKrb5IdParams.
        Specifies the name of the user that performs kadmin tasks.

        :param user: The user of this ProvidersKrb5IdParams.
        :type: str
        """
        
        self._user = user

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

