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


class SettingsAclsAclPolicySettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SettingsAclsAclPolicySettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'access': 'str',
            'calcmode': 'str',
            'calcmode_group': 'str',
            'calcmode_owner': 'str',
            'chmod': 'str',
            'chmod_007': 'str',
            'chmod_inheritable': 'str',
            'chown': 'str',
            'create_over_smb': 'str',
            'dos_attr': 'str',
            'group_owner_inheritance': 'str',
            'rwx': 'str',
            'synthetic_denies': 'str',
            'utimes': 'str'
        }

        self.attribute_map = {
            'access': 'access',
            'calcmode': 'calcmode',
            'calcmode_group': 'calcmode_group',
            'calcmode_owner': 'calcmode_owner',
            'chmod': 'chmod',
            'chmod_007': 'chmod_007',
            'chmod_inheritable': 'chmod_inheritable',
            'chown': 'chown',
            'create_over_smb': 'create_over_smb',
            'dos_attr': 'dos_attr',
            'group_owner_inheritance': 'group_owner_inheritance',
            'rwx': 'rwx',
            'synthetic_denies': 'synthetic_denies',
            'utimes': 'utimes'
        }

        self._access = None
        self._calcmode = None
        self._calcmode_group = None
        self._calcmode_owner = None
        self._chmod = None
        self._chmod_007 = None
        self._chmod_inheritable = None
        self._chown = None
        self._create_over_smb = None
        self._dos_attr = None
        self._group_owner_inheritance = None
        self._rwx = None
        self._synthetic_denies = None
        self._utimes = None

    @property
    def access(self):
        """
        Gets the access of this SettingsAclsAclPolicySettings.
        Access checks (chmod, chown).

        :return: The access of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """
        Sets the access of this SettingsAclsAclPolicySettings.
        Access checks (chmod, chown).

        :param access: The access of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["unix", "windows"]
        if access is not None and access not in allowed_values:
            raise ValueError(
                "Invalid value for `access`, must be one of {0}"
                .format(allowed_values)
            )

        self._access = access

    @property
    def calcmode(self):
        """
        Gets the calcmode of this SettingsAclsAclPolicySettings.
        Displayed mode bits.

        :return: The calcmode of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._calcmode

    @calcmode.setter
    def calcmode(self, calcmode):
        """
        Sets the calcmode of this SettingsAclsAclPolicySettings.
        Displayed mode bits.

        :param calcmode: The calcmode of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["approx", "777"]
        if calcmode is not None and calcmode not in allowed_values:
            raise ValueError(
                "Invalid value for `calcmode`, must be one of {0}"
                .format(allowed_values)
            )

        self._calcmode = calcmode

    @property
    def calcmode_group(self):
        """
        Gets the calcmode_group of this SettingsAclsAclPolicySettings.
        Approximate group mode bits when ACL exists.

        :return: The calcmode_group of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._calcmode_group

    @calcmode_group.setter
    def calcmode_group(self, calcmode_group):
        """
        Sets the calcmode_group of this SettingsAclsAclPolicySettings.
        Approximate group mode bits when ACL exists.

        :param calcmode_group: The calcmode_group of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["group_aces", "group_only"]
        if calcmode_group is not None and calcmode_group not in allowed_values:
            raise ValueError(
                "Invalid value for `calcmode_group`, must be one of {0}"
                .format(allowed_values)
            )

        self._calcmode_group = calcmode_group

    @property
    def calcmode_owner(self):
        """
        Gets the calcmode_owner of this SettingsAclsAclPolicySettings.
        Approximate owner mode bits when ACL exists.

        :return: The calcmode_owner of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._calcmode_owner

    @calcmode_owner.setter
    def calcmode_owner(self, calcmode_owner):
        """
        Sets the calcmode_owner of this SettingsAclsAclPolicySettings.
        Approximate owner mode bits when ACL exists.

        :param calcmode_owner: The calcmode_owner of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["owner_aces", "owner_only"]
        if calcmode_owner is not None and calcmode_owner not in allowed_values:
            raise ValueError(
                "Invalid value for `calcmode_owner`, must be one of {0}"
                .format(allowed_values)
            )

        self._calcmode_owner = calcmode_owner

    @property
    def chmod(self):
        """
        Gets the chmod of this SettingsAclsAclPolicySettings.
        chmod on files with existing ACLs.

        :return: The chmod of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._chmod

    @chmod.setter
    def chmod(self, chmod):
        """
        Sets the chmod of this SettingsAclsAclPolicySettings.
        chmod on files with existing ACLs.

        :param chmod: The chmod of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["remove", "replace", "replace_users_and_groups", "merge", "deny", "ignore"]
        if chmod is not None and chmod not in allowed_values:
            raise ValueError(
                "Invalid value for `chmod`, must be one of {0}"
                .format(allowed_values)
            )

        self._chmod = chmod

    @property
    def chmod_007(self):
        """
        Gets the chmod_007 of this SettingsAclsAclPolicySettings.
        chmod (007) on files with existing ACLs.

        :return: The chmod_007 of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._chmod_007

    @chmod_007.setter
    def chmod_007(self, chmod_007):
        """
        Sets the chmod_007 of this SettingsAclsAclPolicySettings.
        chmod (007) on files with existing ACLs.

        :param chmod_007: The chmod_007 of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["default", "remove"]
        if chmod_007 is not None and chmod_007 not in allowed_values:
            raise ValueError(
                "Invalid value for `chmod_007`, must be one of {0}"
                .format(allowed_values)
            )

        self._chmod_007 = chmod_007

    @property
    def chmod_inheritable(self):
        """
        Gets the chmod_inheritable of this SettingsAclsAclPolicySettings.
        ACLs created on directories by UNIX chmod.

        :return: The chmod_inheritable of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._chmod_inheritable

    @chmod_inheritable.setter
    def chmod_inheritable(self, chmod_inheritable):
        """
        Sets the chmod_inheritable of this SettingsAclsAclPolicySettings.
        ACLs created on directories by UNIX chmod.

        :param chmod_inheritable: The chmod_inheritable of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["yes", "no"]
        if chmod_inheritable is not None and chmod_inheritable not in allowed_values:
            raise ValueError(
                "Invalid value for `chmod_inheritable`, must be one of {0}"
                .format(allowed_values)
            )

        self._chmod_inheritable = chmod_inheritable

    @property
    def chown(self):
        """
        Gets the chown of this SettingsAclsAclPolicySettings.
        chown/chgrp on files with existing ACLs.

        :return: The chown of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._chown

    @chown.setter
    def chown(self, chown):
        """
        Sets the chown of this SettingsAclsAclPolicySettings.
        chown/chgrp on files with existing ACLs.

        :param chown: The chown of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["owner_group_and_acl", "owner_group_only", "ignore"]
        if chown is not None and chown not in allowed_values:
            raise ValueError(
                "Invalid value for `chown`, must be one of {0}"
                .format(allowed_values)
            )

        self._chown = chown

    @property
    def create_over_smb(self):
        """
        Gets the create_over_smb of this SettingsAclsAclPolicySettings.
        ACL creation over SMB.

        :return: The create_over_smb of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._create_over_smb

    @create_over_smb.setter
    def create_over_smb(self, create_over_smb):
        """
        Sets the create_over_smb of this SettingsAclsAclPolicySettings.
        ACL creation over SMB.

        :param create_over_smb: The create_over_smb of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["allow", "disallow"]
        if create_over_smb is not None and create_over_smb not in allowed_values:
            raise ValueError(
                "Invalid value for `create_over_smb`, must be one of {0}"
                .format(allowed_values)
            )

        self._create_over_smb = create_over_smb

    @property
    def dos_attr(self):
        """
        Gets the dos_attr of this SettingsAclsAclPolicySettings.
         Read only DOS attribute.

        :return: The dos_attr of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._dos_attr

    @dos_attr.setter
    def dos_attr(self, dos_attr):
        """
        Sets the dos_attr of this SettingsAclsAclPolicySettings.
         Read only DOS attribute.

        :param dos_attr: The dos_attr of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["deny_smb", "deny_smb_and_nfs"]
        if dos_attr is not None and dos_attr not in allowed_values:
            raise ValueError(
                "Invalid value for `dos_attr`, must be one of {0}"
                .format(allowed_values)
            )

        self._dos_attr = dos_attr

    @property
    def group_owner_inheritance(self):
        """
        Gets the group_owner_inheritance of this SettingsAclsAclPolicySettings.
        Group owner inheritance.

        :return: The group_owner_inheritance of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._group_owner_inheritance

    @group_owner_inheritance.setter
    def group_owner_inheritance(self, group_owner_inheritance):
        """
        Sets the group_owner_inheritance of this SettingsAclsAclPolicySettings.
        Group owner inheritance.

        :param group_owner_inheritance: The group_owner_inheritance of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["native", "parent", "creator"]
        if group_owner_inheritance is not None and group_owner_inheritance not in allowed_values:
            raise ValueError(
                "Invalid value for `group_owner_inheritance`, must be one of {0}"
                .format(allowed_values)
            )

        self._group_owner_inheritance = group_owner_inheritance

    @property
    def rwx(self):
        """
        Gets the rwx of this SettingsAclsAclPolicySettings.
        Treatment of 'rwx' permissions.

        :return: The rwx of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._rwx

    @rwx.setter
    def rwx(self, rwx):
        """
        Sets the rwx of this SettingsAclsAclPolicySettings.
        Treatment of 'rwx' permissions.

        :param rwx: The rwx of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["retain", "full_control"]
        if rwx is not None and rwx not in allowed_values:
            raise ValueError(
                "Invalid value for `rwx`, must be one of {0}"
                .format(allowed_values)
            )

        self._rwx = rwx

    @property
    def synthetic_denies(self):
        """
        Gets the synthetic_denies of this SettingsAclsAclPolicySettings.
        Synthetic 'deny' ACEs.

        :return: The synthetic_denies of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._synthetic_denies

    @synthetic_denies.setter
    def synthetic_denies(self, synthetic_denies):
        """
        Sets the synthetic_denies of this SettingsAclsAclPolicySettings.
        Synthetic 'deny' ACEs.

        :param synthetic_denies: The synthetic_denies of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["none", "remove"]
        if synthetic_denies is not None and synthetic_denies not in allowed_values:
            raise ValueError(
                "Invalid value for `synthetic_denies`, must be one of {0}"
                .format(allowed_values)
            )

        self._synthetic_denies = synthetic_denies

    @property
    def utimes(self):
        """
        Gets the utimes of this SettingsAclsAclPolicySettings.
        Access check (utimes)

        :return: The utimes of this SettingsAclsAclPolicySettings.
        :rtype: str
        """
        return self._utimes

    @utimes.setter
    def utimes(self, utimes):
        """
        Sets the utimes of this SettingsAclsAclPolicySettings.
        Access check (utimes)

        :param utimes: The utimes of this SettingsAclsAclPolicySettings.
        :type: str
        """
        allowed_values = ["only_owner", "owner_and_write"]
        if utimes is not None and utimes not in allowed_values:
            raise ValueError(
                "Invalid value for `utimes`, must be one of {0}"
                .format(allowed_values)
            )

        self._utimes = utimes

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

