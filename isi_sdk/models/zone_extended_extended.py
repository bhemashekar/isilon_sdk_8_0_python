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


class ZoneExtendedExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ZoneExtendedExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'alternate_system_provider': 'str',
            'auth_providers': 'list[str]',
            'cache_entry_expiry': 'int',
            'create_path': 'bool',
            'groupnet': 'str',
            'home_directory_umask': 'int',
            'id': 'str',
            'ifs_restricted': 'list[GroupMember]',
            'map_untrusted': 'str',
            'name': 'str',
            'netbios_name': 'str',
            'path': 'str',
            'skeleton_directory': 'str',
            'system': 'bool',
            'system_provider': 'str',
            'user_mapping_rules': 'list[str]',
            'zone_id': 'int'
        }

        self.attribute_map = {
            'alternate_system_provider': 'alternate_system_provider',
            'auth_providers': 'auth_providers',
            'cache_entry_expiry': 'cache_entry_expiry',
            'create_path': 'create_path',
            'groupnet': 'groupnet',
            'home_directory_umask': 'home_directory_umask',
            'id': 'id',
            'ifs_restricted': 'ifs_restricted',
            'map_untrusted': 'map_untrusted',
            'name': 'name',
            'netbios_name': 'netbios_name',
            'path': 'path',
            'skeleton_directory': 'skeleton_directory',
            'system': 'system',
            'system_provider': 'system_provider',
            'user_mapping_rules': 'user_mapping_rules',
            'zone_id': 'zone_id'
        }

        self._alternate_system_provider = None
        self._auth_providers = None
        self._cache_entry_expiry = None
        self._create_path = None
        self._groupnet = None
        self._home_directory_umask = None
        self._id = None
        self._ifs_restricted = None
        self._map_untrusted = None
        self._name = None
        self._netbios_name = None
        self._path = None
        self._skeleton_directory = None
        self._system = None
        self._system_provider = None
        self._user_mapping_rules = None
        self._zone_id = None

    @property
    def alternate_system_provider(self):
        """
        Gets the alternate_system_provider of this ZoneExtendedExtended.
        Specifies an alternate system provider.

        :return: The alternate_system_provider of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._alternate_system_provider

    @alternate_system_provider.setter
    def alternate_system_provider(self, alternate_system_provider):
        """
        Sets the alternate_system_provider of this ZoneExtendedExtended.
        Specifies an alternate system provider.

        :param alternate_system_provider: The alternate_system_provider of this ZoneExtendedExtended.
        :type: str
        """
        
        self._alternate_system_provider = alternate_system_provider

    @property
    def auth_providers(self):
        """
        Gets the auth_providers of this ZoneExtendedExtended.
        Specifies the list of authentication providers available on this access zone.

        :return: The auth_providers of this ZoneExtendedExtended.
        :rtype: list[str]
        """
        return self._auth_providers

    @auth_providers.setter
    def auth_providers(self, auth_providers):
        """
        Sets the auth_providers of this ZoneExtendedExtended.
        Specifies the list of authentication providers available on this access zone.

        :param auth_providers: The auth_providers of this ZoneExtendedExtended.
        :type: list[str]
        """
        
        self._auth_providers = auth_providers

    @property
    def cache_entry_expiry(self):
        """
        Gets the cache_entry_expiry of this ZoneExtendedExtended.
        Specifies amount of time in seconds to cache a user/group.

        :return: The cache_entry_expiry of this ZoneExtendedExtended.
        :rtype: int
        """
        return self._cache_entry_expiry

    @cache_entry_expiry.setter
    def cache_entry_expiry(self, cache_entry_expiry):
        """
        Sets the cache_entry_expiry of this ZoneExtendedExtended.
        Specifies amount of time in seconds to cache a user/group.

        :param cache_entry_expiry: The cache_entry_expiry of this ZoneExtendedExtended.
        :type: int
        """
        
        self._cache_entry_expiry = cache_entry_expiry

    @property
    def create_path(self):
        """
        Gets the create_path of this ZoneExtendedExtended.
        Determines if a path is created when a path does not exist.

        :return: The create_path of this ZoneExtendedExtended.
        :rtype: bool
        """
        return self._create_path

    @create_path.setter
    def create_path(self, create_path):
        """
        Sets the create_path of this ZoneExtendedExtended.
        Determines if a path is created when a path does not exist.

        :param create_path: The create_path of this ZoneExtendedExtended.
        :type: bool
        """
        
        self._create_path = create_path

    @property
    def groupnet(self):
        """
        Gets the groupnet of this ZoneExtendedExtended.
        Groupnet identitier

        :return: The groupnet of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """
        Sets the groupnet of this ZoneExtendedExtended.
        Groupnet identitier

        :param groupnet: The groupnet of this ZoneExtendedExtended.
        :type: str
        """
        
        self._groupnet = groupnet

    @property
    def home_directory_umask(self):
        """
        Gets the home_directory_umask of this ZoneExtendedExtended.
        Specifies the permissions set on automatically created user home directories.

        :return: The home_directory_umask of this ZoneExtendedExtended.
        :rtype: int
        """
        return self._home_directory_umask

    @home_directory_umask.setter
    def home_directory_umask(self, home_directory_umask):
        """
        Sets the home_directory_umask of this ZoneExtendedExtended.
        Specifies the permissions set on automatically created user home directories.

        :param home_directory_umask: The home_directory_umask of this ZoneExtendedExtended.
        :type: int
        """
        
        self._home_directory_umask = home_directory_umask

    @property
    def id(self):
        """
        Gets the id of this ZoneExtendedExtended.
        Specifies the system-assigned ID for the access zone. This value is returned when an access zone is created through the POST method

        :return: The id of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ZoneExtendedExtended.
        Specifies the system-assigned ID for the access zone. This value is returned when an access zone is created through the POST method

        :param id: The id of this ZoneExtendedExtended.
        :type: str
        """
        
        self._id = id

    @property
    def ifs_restricted(self):
        """
        Gets the ifs_restricted of this ZoneExtendedExtended.
        Specifies a list of users and groups that have read and write access to /ifs.

        :return: The ifs_restricted of this ZoneExtendedExtended.
        :rtype: list[GroupMember]
        """
        return self._ifs_restricted

    @ifs_restricted.setter
    def ifs_restricted(self, ifs_restricted):
        """
        Sets the ifs_restricted of this ZoneExtendedExtended.
        Specifies a list of users and groups that have read and write access to /ifs.

        :param ifs_restricted: The ifs_restricted of this ZoneExtendedExtended.
        :type: list[GroupMember]
        """
        
        self._ifs_restricted = ifs_restricted

    @property
    def map_untrusted(self):
        """
        Gets the map_untrusted of this ZoneExtendedExtended.
        Maps untrusted domains to this NetBIOS domain during authentication.

        :return: The map_untrusted of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._map_untrusted

    @map_untrusted.setter
    def map_untrusted(self, map_untrusted):
        """
        Sets the map_untrusted of this ZoneExtendedExtended.
        Maps untrusted domains to this NetBIOS domain during authentication.

        :param map_untrusted: The map_untrusted of this ZoneExtendedExtended.
        :type: str
        """
        
        self._map_untrusted = map_untrusted

    @property
    def name(self):
        """
        Gets the name of this ZoneExtendedExtended.
        Specifies the access zone name.

        :return: The name of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ZoneExtendedExtended.
        Specifies the access zone name.

        :param name: The name of this ZoneExtendedExtended.
        :type: str
        """
        
        self._name = name

    @property
    def netbios_name(self):
        """
        Gets the netbios_name of this ZoneExtendedExtended.
        Specifies the NetBIOS name.

        :return: The netbios_name of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._netbios_name

    @netbios_name.setter
    def netbios_name(self, netbios_name):
        """
        Sets the netbios_name of this ZoneExtendedExtended.
        Specifies the NetBIOS name.

        :param netbios_name: The netbios_name of this ZoneExtendedExtended.
        :type: str
        """
        
        self._netbios_name = netbios_name

    @property
    def path(self):
        """
        Gets the path of this ZoneExtendedExtended.
        Specifies the access zone base directory path.

        :return: The path of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ZoneExtendedExtended.
        Specifies the access zone base directory path.

        :param path: The path of this ZoneExtendedExtended.
        :type: str
        """
        
        self._path = path

    @property
    def skeleton_directory(self):
        """
        Gets the skeleton_directory of this ZoneExtendedExtended.
        Specifies the skeleton directory that is used for user home directories.

        :return: The skeleton_directory of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._skeleton_directory

    @skeleton_directory.setter
    def skeleton_directory(self, skeleton_directory):
        """
        Sets the skeleton_directory of this ZoneExtendedExtended.
        Specifies the skeleton directory that is used for user home directories.

        :param skeleton_directory: The skeleton_directory of this ZoneExtendedExtended.
        :type: str
        """
        
        self._skeleton_directory = skeleton_directory

    @property
    def system(self):
        """
        Gets the system of this ZoneExtendedExtended.
        True if the access zone is built-in.

        :return: The system of this ZoneExtendedExtended.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this ZoneExtendedExtended.
        True if the access zone is built-in.

        :param system: The system of this ZoneExtendedExtended.
        :type: bool
        """
        
        self._system = system

    @property
    def system_provider(self):
        """
        Gets the system_provider of this ZoneExtendedExtended.
        Specifies the system provider for the access zone.

        :return: The system_provider of this ZoneExtendedExtended.
        :rtype: str
        """
        return self._system_provider

    @system_provider.setter
    def system_provider(self, system_provider):
        """
        Sets the system_provider of this ZoneExtendedExtended.
        Specifies the system provider for the access zone.

        :param system_provider: The system_provider of this ZoneExtendedExtended.
        :type: str
        """
        
        self._system_provider = system_provider

    @property
    def user_mapping_rules(self):
        """
        Gets the user_mapping_rules of this ZoneExtendedExtended.
        Specifies the current ID mapping rules.

        :return: The user_mapping_rules of this ZoneExtendedExtended.
        :rtype: list[str]
        """
        return self._user_mapping_rules

    @user_mapping_rules.setter
    def user_mapping_rules(self, user_mapping_rules):
        """
        Sets the user_mapping_rules of this ZoneExtendedExtended.
        Specifies the current ID mapping rules.

        :param user_mapping_rules: The user_mapping_rules of this ZoneExtendedExtended.
        :type: list[str]
        """
        
        self._user_mapping_rules = user_mapping_rules

    @property
    def zone_id(self):
        """
        Gets the zone_id of this ZoneExtendedExtended.
        Specifies the access zone ID on the system.

        :return: The zone_id of this ZoneExtendedExtended.
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """
        Sets the zone_id of this ZoneExtendedExtended.
        Specifies the access zone ID on the system.

        :param zone_id: The zone_id of this ZoneExtendedExtended.
        :type: int
        """
        
        self._zone_id = zone_id

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

