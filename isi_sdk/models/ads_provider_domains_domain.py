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


class AdsProviderDomainsDomain(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AdsProviderDomainsDomain - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'client_site': 'str',
            'dc_address': 'str',
            'dc_name': 'str',
            'dc_site': 'str',
            'domain': 'str',
            'guid': 'str',
            'id': 'str',
            'netbios_name': 'str',
            'sid': 'str',
            'status': 'str',
            'trust_type': 'str'
        }

        self.attribute_map = {
            'client_site': 'client_site',
            'dc_address': 'dc_address',
            'dc_name': 'dc_name',
            'dc_site': 'dc_site',
            'domain': 'domain',
            'guid': 'guid',
            'id': 'id',
            'netbios_name': 'netbios_name',
            'sid': 'sid',
            'status': 'status',
            'trust_type': 'trust_type'
        }

        self._client_site = None
        self._dc_address = None
        self._dc_name = None
        self._dc_site = None
        self._domain = None
        self._guid = None
        self._id = None
        self._netbios_name = None
        self._sid = None
        self._status = None
        self._trust_type = None

    @property
    def client_site(self):
        """
        Gets the client_site of this AdsProviderDomainsDomain.
        The Nodes Site.

        :return: The client_site of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._client_site

    @client_site.setter
    def client_site(self, client_site):
        """
        Sets the client_site of this AdsProviderDomainsDomain.
        The Nodes Site.

        :param client_site: The client_site of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._client_site = client_site

    @property
    def dc_address(self):
        """
        Gets the dc_address of this AdsProviderDomainsDomain.
        Specifies the address for the domain controller.

        :return: The dc_address of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._dc_address

    @dc_address.setter
    def dc_address(self, dc_address):
        """
        Sets the dc_address of this AdsProviderDomainsDomain.
        Specifies the address for the domain controller.

        :param dc_address: The dc_address of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._dc_address = dc_address

    @property
    def dc_name(self):
        """
        Gets the dc_name of this AdsProviderDomainsDomain.
        Specifies the name for the domain controller.

        :return: The dc_name of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._dc_name

    @dc_name.setter
    def dc_name(self, dc_name):
        """
        Sets the dc_name of this AdsProviderDomainsDomain.
        Specifies the name for the domain controller.

        :param dc_name: The dc_name of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._dc_name = dc_name

    @property
    def dc_site(self):
        """
        Gets the dc_site of this AdsProviderDomainsDomain.
        Specifies the site for the domain controller.

        :return: The dc_site of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._dc_site

    @dc_site.setter
    def dc_site(self, dc_site):
        """
        Sets the dc_site of this AdsProviderDomainsDomain.
        Specifies the site for the domain controller.

        :param dc_site: The dc_site of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._dc_site = dc_site

    @property
    def domain(self):
        """
        Gets the domain of this AdsProviderDomainsDomain.
        Specifies the name of the domain.

        :return: The domain of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this AdsProviderDomainsDomain.
        Specifies the name of the domain.

        :param domain: The domain of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._domain = domain

    @property
    def guid(self):
        """
        Gets the guid of this AdsProviderDomainsDomain.
        Specifies the globally unique ID for the domain.

        :return: The guid of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """
        Sets the guid of this AdsProviderDomainsDomain.
        Specifies the globally unique ID for the domain.

        :param guid: The guid of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._guid = guid

    @property
    def id(self):
        """
        Gets the id of this AdsProviderDomainsDomain.
        Specifies a unique identifier for every domain returned.

        :return: The id of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AdsProviderDomainsDomain.
        Specifies a unique identifier for every domain returned.

        :param id: The id of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._id = id

    @property
    def netbios_name(self):
        """
        Gets the netbios_name of this AdsProviderDomainsDomain.
        Specifies the NetBIOS name for the domain.

        :return: The netbios_name of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._netbios_name

    @netbios_name.setter
    def netbios_name(self, netbios_name):
        """
        Sets the netbios_name of this AdsProviderDomainsDomain.
        Specifies the NetBIOS name for the domain.

        :param netbios_name: The netbios_name of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._netbios_name = netbios_name

    @property
    def sid(self):
        """
        Gets the sid of this AdsProviderDomainsDomain.
        Specifies the security ID for the domain.

        :return: The sid of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this AdsProviderDomainsDomain.
        Specifies the security ID for the domain.

        :param sid: The sid of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._sid = sid

    @property
    def status(self):
        """
        Gets the status of this AdsProviderDomainsDomain.
        Specifies the status of the domain.

        :return: The status of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AdsProviderDomainsDomain.
        Specifies the status of the domain.

        :param status: The status of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._status = status

    @property
    def trust_type(self):
        """
        Gets the trust_type of this AdsProviderDomainsDomain.
        Specifies the type of trust for this domain. Options include 'primary', 'unknown', 'external', and 'forest'.

        :return: The trust_type of this AdsProviderDomainsDomain.
        :rtype: str
        """
        return self._trust_type

    @trust_type.setter
    def trust_type(self, trust_type):
        """
        Sets the trust_type of this AdsProviderDomainsDomain.
        Specifies the type of trust for this domain. Options include 'primary', 'unknown', 'external', and 'forest'.

        :param trust_type: The trust_type of this AdsProviderDomainsDomain.
        :type: str
        """
        
        self._trust_type = trust_type

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

