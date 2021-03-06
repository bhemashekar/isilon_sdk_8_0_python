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


class AntivirusSettingsSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AntivirusSettingsSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'fail_open': 'bool',
            'glob_filters': 'list[str]',
            'glob_filters_enabled': 'bool',
            'glob_filters_include': 'bool',
            'path_prefixes': 'list[str]',
            'quarantine': 'bool',
            'repair': 'bool',
            'report_expiry': 'int',
            'scan_on_close': 'bool',
            'scan_on_open': 'bool',
            'scan_size_maximum': 'int',
            'service': 'bool',
            'truncate': 'bool'
        }

        self.attribute_map = {
            'fail_open': 'fail_open',
            'glob_filters': 'glob_filters',
            'glob_filters_enabled': 'glob_filters_enabled',
            'glob_filters_include': 'glob_filters_include',
            'path_prefixes': 'path_prefixes',
            'quarantine': 'quarantine',
            'repair': 'repair',
            'report_expiry': 'report_expiry',
            'scan_on_close': 'scan_on_close',
            'scan_on_open': 'scan_on_open',
            'scan_size_maximum': 'scan_size_maximum',
            'service': 'service',
            'truncate': 'truncate'
        }

        self._fail_open = None
        self._glob_filters = None
        self._glob_filters_enabled = None
        self._glob_filters_include = None
        self._path_prefixes = None
        self._quarantine = None
        self._repair = None
        self._report_expiry = None
        self._scan_on_close = None
        self._scan_on_open = None
        self._scan_size_maximum = None
        self._service = None
        self._truncate = None

    @property
    def fail_open(self):
        """
        Gets the fail_open of this AntivirusSettingsSettings.
        Allow access when scanning fails.

        :return: The fail_open of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._fail_open

    @fail_open.setter
    def fail_open(self, fail_open):
        """
        Sets the fail_open of this AntivirusSettingsSettings.
        Allow access when scanning fails.

        :param fail_open: The fail_open of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._fail_open = fail_open

    @property
    def glob_filters(self):
        """
        Gets the glob_filters of this AntivirusSettingsSettings.
        Glob patterns for leaf filenames.

        :return: The glob_filters of this AntivirusSettingsSettings.
        :rtype: list[str]
        """
        return self._glob_filters

    @glob_filters.setter
    def glob_filters(self, glob_filters):
        """
        Sets the glob_filters of this AntivirusSettingsSettings.
        Glob patterns for leaf filenames.

        :param glob_filters: The glob_filters of this AntivirusSettingsSettings.
        :type: list[str]
        """
        
        self._glob_filters = glob_filters

    @property
    def glob_filters_enabled(self):
        """
        Gets the glob_filters_enabled of this AntivirusSettingsSettings.
        Enable glob filters.

        :return: The glob_filters_enabled of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._glob_filters_enabled

    @glob_filters_enabled.setter
    def glob_filters_enabled(self, glob_filters_enabled):
        """
        Sets the glob_filters_enabled of this AntivirusSettingsSettings.
        Enable glob filters.

        :param glob_filters_enabled: The glob_filters_enabled of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._glob_filters_enabled = glob_filters_enabled

    @property
    def glob_filters_include(self):
        """
        Gets the glob_filters_include of this AntivirusSettingsSettings.
        If true, only scan files matching a glob filter. If false, only scan files that don't match a glob filter.

        :return: The glob_filters_include of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._glob_filters_include

    @glob_filters_include.setter
    def glob_filters_include(self, glob_filters_include):
        """
        Sets the glob_filters_include of this AntivirusSettingsSettings.
        If true, only scan files matching a glob filter. If false, only scan files that don't match a glob filter.

        :param glob_filters_include: The glob_filters_include of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._glob_filters_include = glob_filters_include

    @property
    def path_prefixes(self):
        """
        Gets the path_prefixes of this AntivirusSettingsSettings.
        Paths to include in realtime scans.

        :return: The path_prefixes of this AntivirusSettingsSettings.
        :rtype: list[str]
        """
        return self._path_prefixes

    @path_prefixes.setter
    def path_prefixes(self, path_prefixes):
        """
        Sets the path_prefixes of this AntivirusSettingsSettings.
        Paths to include in realtime scans.

        :param path_prefixes: The path_prefixes of this AntivirusSettingsSettings.
        :type: list[str]
        """
        
        self._path_prefixes = path_prefixes

    @property
    def quarantine(self):
        """
        Gets the quarantine of this AntivirusSettingsSettings.
        Try to quarantine files when threats are found.

        :return: The quarantine of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._quarantine

    @quarantine.setter
    def quarantine(self, quarantine):
        """
        Sets the quarantine of this AntivirusSettingsSettings.
        Try to quarantine files when threats are found.

        :param quarantine: The quarantine of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._quarantine = quarantine

    @property
    def repair(self):
        """
        Gets the repair of this AntivirusSettingsSettings.
        Try to repair files when threats are found.

        :return: The repair of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._repair

    @repair.setter
    def repair(self, repair):
        """
        Sets the repair of this AntivirusSettingsSettings.
        Try to repair files when threats are found.

        :param repair: The repair of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._repair = repair

    @property
    def report_expiry(self):
        """
        Gets the report_expiry of this AntivirusSettingsSettings.
        Amount of time in seconds until old reporting data is purged.

        :return: The report_expiry of this AntivirusSettingsSettings.
        :rtype: int
        """
        return self._report_expiry

    @report_expiry.setter
    def report_expiry(self, report_expiry):
        """
        Sets the report_expiry of this AntivirusSettingsSettings.
        Amount of time in seconds until old reporting data is purged.

        :param report_expiry: The report_expiry of this AntivirusSettingsSettings.
        :type: int
        """
        
        if not report_expiry:
            raise ValueError("Invalid value for `report_expiry`, must not be `None`")
        if report_expiry < 0.0: 
            raise ValueError("Invalid value for `report_expiry`, must be a value greater than or equal to `0.0`")

        self._report_expiry = report_expiry

    @property
    def scan_on_close(self):
        """
        Gets the scan_on_close of this AntivirusSettingsSettings.
        Scan files when apps close them.

        :return: The scan_on_close of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._scan_on_close

    @scan_on_close.setter
    def scan_on_close(self, scan_on_close):
        """
        Sets the scan_on_close of this AntivirusSettingsSettings.
        Scan files when apps close them.

        :param scan_on_close: The scan_on_close of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._scan_on_close = scan_on_close

    @property
    def scan_on_open(self):
        """
        Gets the scan_on_open of this AntivirusSettingsSettings.
        Scan files on access.

        :return: The scan_on_open of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._scan_on_open

    @scan_on_open.setter
    def scan_on_open(self, scan_on_open):
        """
        Sets the scan_on_open of this AntivirusSettingsSettings.
        Scan files on access.

        :param scan_on_open: The scan_on_open of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._scan_on_open = scan_on_open

    @property
    def scan_size_maximum(self):
        """
        Gets the scan_size_maximum of this AntivirusSettingsSettings.
        Skip scanning files larger than this.

        :return: The scan_size_maximum of this AntivirusSettingsSettings.
        :rtype: int
        """
        return self._scan_size_maximum

    @scan_size_maximum.setter
    def scan_size_maximum(self, scan_size_maximum):
        """
        Sets the scan_size_maximum of this AntivirusSettingsSettings.
        Skip scanning files larger than this.

        :param scan_size_maximum: The scan_size_maximum of this AntivirusSettingsSettings.
        :type: int
        """
        
        if not scan_size_maximum:
            raise ValueError("Invalid value for `scan_size_maximum`, must not be `None`")
        if scan_size_maximum < 0.0: 
            raise ValueError("Invalid value for `scan_size_maximum`, must be a value greater than or equal to `0.0`")

        self._scan_size_maximum = scan_size_maximum

    @property
    def service(self):
        """
        Gets the service of this AntivirusSettingsSettings.
        Whether the antivirus service is enabled.

        :return: The service of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this AntivirusSettingsSettings.
        Whether the antivirus service is enabled.

        :param service: The service of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._service = service

    @property
    def truncate(self):
        """
        Gets the truncate of this AntivirusSettingsSettings.
        Try to truncate files when threats are found.

        :return: The truncate of this AntivirusSettingsSettings.
        :rtype: bool
        """
        return self._truncate

    @truncate.setter
    def truncate(self, truncate):
        """
        Sets the truncate of this AntivirusSettingsSettings.
        Try to truncate files when threats are found.

        :param truncate: The truncate of this AntivirusSettingsSettings.
        :type: bool
        """
        
        self._truncate = truncate

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

