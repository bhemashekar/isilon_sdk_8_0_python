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


class FtpSettingsSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FtpSettingsSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'accept_timeout': 'int',
            'allow_anon_access': 'bool',
            'allow_anon_upload': 'bool',
            'allow_dirlists': 'bool',
            'allow_downloads': 'bool',
            'allow_local_access': 'bool',
            'allow_writes': 'bool',
            'always_chdir_homedir': 'bool',
            'anon_chown_username': 'str',
            'anon_password_list': 'list[str]',
            'anon_root_path': 'str',
            'anon_umask': 'int',
            'ascii_mode': 'str',
            'chroot_exception_list': 'list[str]',
            'chroot_local_mode': 'str',
            'connect_timeout': 'int',
            'data_timeout': 'int',
            'denied_user_list': 'list[str]',
            'dirlist_localtime': 'bool',
            'dirlist_names': 'str',
            'file_create_perm': 'int',
            'limit_anon_passwords': 'bool',
            'local_root_path': 'str',
            'local_umask': 'int',
            'server_to_server': 'bool',
            'service': 'bool',
            'session_support': 'bool',
            'session_timeout': 'int',
            'user_config_dir': 'str'
        }

        self.attribute_map = {
            'accept_timeout': 'accept_timeout',
            'allow_anon_access': 'allow_anon_access',
            'allow_anon_upload': 'allow_anon_upload',
            'allow_dirlists': 'allow_dirlists',
            'allow_downloads': 'allow_downloads',
            'allow_local_access': 'allow_local_access',
            'allow_writes': 'allow_writes',
            'always_chdir_homedir': 'always_chdir_homedir',
            'anon_chown_username': 'anon_chown_username',
            'anon_password_list': 'anon_password_list',
            'anon_root_path': 'anon_root_path',
            'anon_umask': 'anon_umask',
            'ascii_mode': 'ascii_mode',
            'chroot_exception_list': 'chroot_exception_list',
            'chroot_local_mode': 'chroot_local_mode',
            'connect_timeout': 'connect_timeout',
            'data_timeout': 'data_timeout',
            'denied_user_list': 'denied_user_list',
            'dirlist_localtime': 'dirlist_localtime',
            'dirlist_names': 'dirlist_names',
            'file_create_perm': 'file_create_perm',
            'limit_anon_passwords': 'limit_anon_passwords',
            'local_root_path': 'local_root_path',
            'local_umask': 'local_umask',
            'server_to_server': 'server_to_server',
            'service': 'service',
            'session_support': 'session_support',
            'session_timeout': 'session_timeout',
            'user_config_dir': 'user_config_dir'
        }

        self._accept_timeout = None
        self._allow_anon_access = None
        self._allow_anon_upload = None
        self._allow_dirlists = None
        self._allow_downloads = None
        self._allow_local_access = None
        self._allow_writes = None
        self._always_chdir_homedir = None
        self._anon_chown_username = None
        self._anon_password_list = None
        self._anon_root_path = None
        self._anon_umask = None
        self._ascii_mode = None
        self._chroot_exception_list = None
        self._chroot_local_mode = None
        self._connect_timeout = None
        self._data_timeout = None
        self._denied_user_list = None
        self._dirlist_localtime = None
        self._dirlist_names = None
        self._file_create_perm = None
        self._limit_anon_passwords = None
        self._local_root_path = None
        self._local_umask = None
        self._server_to_server = None
        self._service = None
        self._session_support = None
        self._session_timeout = None
        self._user_config_dir = None

    @property
    def accept_timeout(self):
        """
        Gets the accept_timeout of this FtpSettingsSettings.
        The timeout, in seconds, for a remote client to establish a PASV style data connection.

        :return: The accept_timeout of this FtpSettingsSettings.
        :rtype: int
        """
        return self._accept_timeout

    @accept_timeout.setter
    def accept_timeout(self, accept_timeout):
        """
        Sets the accept_timeout of this FtpSettingsSettings.
        The timeout, in seconds, for a remote client to establish a PASV style data connection.

        :param accept_timeout: The accept_timeout of this FtpSettingsSettings.
        :type: int
        """
        
        if not accept_timeout:
            raise ValueError("Invalid value for `accept_timeout`, must not be `None`")
        if accept_timeout > 600.0: 
            raise ValueError("Invalid value for `accept_timeout`, must be a value less than or equal to `600.0`")
        if accept_timeout < 30.0: 
            raise ValueError("Invalid value for `accept_timeout`, must be a value greater than or equal to `30.0`")

        self._accept_timeout = accept_timeout

    @property
    def allow_anon_access(self):
        """
        Gets the allow_anon_access of this FtpSettingsSettings.
        Controls whether anonymous logins are permitted or not.

        :return: The allow_anon_access of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._allow_anon_access

    @allow_anon_access.setter
    def allow_anon_access(self, allow_anon_access):
        """
        Sets the allow_anon_access of this FtpSettingsSettings.
        Controls whether anonymous logins are permitted or not.

        :param allow_anon_access: The allow_anon_access of this FtpSettingsSettings.
        :type: bool
        """
        
        self._allow_anon_access = allow_anon_access

    @property
    def allow_anon_upload(self):
        """
        Gets the allow_anon_upload of this FtpSettingsSettings.
        Controls whether anonymous users will be permitted to upload files.

        :return: The allow_anon_upload of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._allow_anon_upload

    @allow_anon_upload.setter
    def allow_anon_upload(self, allow_anon_upload):
        """
        Sets the allow_anon_upload of this FtpSettingsSettings.
        Controls whether anonymous users will be permitted to upload files.

        :param allow_anon_upload: The allow_anon_upload of this FtpSettingsSettings.
        :type: bool
        """
        
        self._allow_anon_upload = allow_anon_upload

    @property
    def allow_dirlists(self):
        """
        Gets the allow_dirlists of this FtpSettingsSettings.
        If set to false, all directory list commands will return a permission denied error.

        :return: The allow_dirlists of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._allow_dirlists

    @allow_dirlists.setter
    def allow_dirlists(self, allow_dirlists):
        """
        Sets the allow_dirlists of this FtpSettingsSettings.
        If set to false, all directory list commands will return a permission denied error.

        :param allow_dirlists: The allow_dirlists of this FtpSettingsSettings.
        :type: bool
        """
        
        self._allow_dirlists = allow_dirlists

    @property
    def allow_downloads(self):
        """
        Gets the allow_downloads of this FtpSettingsSettings.
        If set to false, all downloads requests will return a permission denied error.

        :return: The allow_downloads of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._allow_downloads

    @allow_downloads.setter
    def allow_downloads(self, allow_downloads):
        """
        Sets the allow_downloads of this FtpSettingsSettings.
        If set to false, all downloads requests will return a permission denied error.

        :param allow_downloads: The allow_downloads of this FtpSettingsSettings.
        :type: bool
        """
        
        self._allow_downloads = allow_downloads

    @property
    def allow_local_access(self):
        """
        Gets the allow_local_access of this FtpSettingsSettings.
        Controls whether local logins are permitted or not.

        :return: The allow_local_access of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._allow_local_access

    @allow_local_access.setter
    def allow_local_access(self, allow_local_access):
        """
        Sets the allow_local_access of this FtpSettingsSettings.
        Controls whether local logins are permitted or not.

        :param allow_local_access: The allow_local_access of this FtpSettingsSettings.
        :type: bool
        """
        
        self._allow_local_access = allow_local_access

    @property
    def allow_writes(self):
        """
        Gets the allow_writes of this FtpSettingsSettings.
        This controls whether any FTP commands which change the filesystem are allowed or not.

        :return: The allow_writes of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._allow_writes

    @allow_writes.setter
    def allow_writes(self, allow_writes):
        """
        Sets the allow_writes of this FtpSettingsSettings.
        This controls whether any FTP commands which change the filesystem are allowed or not.

        :param allow_writes: The allow_writes of this FtpSettingsSettings.
        :type: bool
        """
        
        self._allow_writes = allow_writes

    @property
    def always_chdir_homedir(self):
        """
        Gets the always_chdir_homedir of this FtpSettingsSettings.
        This controls whether FTP will always initially change directories to the home directory of the user, regardless of whether it is chroot-ing.

        :return: The always_chdir_homedir of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._always_chdir_homedir

    @always_chdir_homedir.setter
    def always_chdir_homedir(self, always_chdir_homedir):
        """
        Sets the always_chdir_homedir of this FtpSettingsSettings.
        This controls whether FTP will always initially change directories to the home directory of the user, regardless of whether it is chroot-ing.

        :param always_chdir_homedir: The always_chdir_homedir of this FtpSettingsSettings.
        :type: bool
        """
        
        self._always_chdir_homedir = always_chdir_homedir

    @property
    def anon_chown_username(self):
        """
        Gets the anon_chown_username of this FtpSettingsSettings.
        This is the name of the user who is given ownership of anonymously uploaded files.

        :return: The anon_chown_username of this FtpSettingsSettings.
        :rtype: str
        """
        return self._anon_chown_username

    @anon_chown_username.setter
    def anon_chown_username(self, anon_chown_username):
        """
        Sets the anon_chown_username of this FtpSettingsSettings.
        This is the name of the user who is given ownership of anonymously uploaded files.

        :param anon_chown_username: The anon_chown_username of this FtpSettingsSettings.
        :type: str
        """
        
        self._anon_chown_username = anon_chown_username

    @property
    def anon_password_list(self):
        """
        Gets the anon_password_list of this FtpSettingsSettings.
        A list of passwords for anonymous users.

        :return: The anon_password_list of this FtpSettingsSettings.
        :rtype: list[str]
        """
        return self._anon_password_list

    @anon_password_list.setter
    def anon_password_list(self, anon_password_list):
        """
        Sets the anon_password_list of this FtpSettingsSettings.
        A list of passwords for anonymous users.

        :param anon_password_list: The anon_password_list of this FtpSettingsSettings.
        :type: list[str]
        """
        
        self._anon_password_list = anon_password_list

    @property
    def anon_root_path(self):
        """
        Gets the anon_root_path of this FtpSettingsSettings.
        This option represents a directory in /ifs which vsftpd will try to change into after an anonymous login.

        :return: The anon_root_path of this FtpSettingsSettings.
        :rtype: str
        """
        return self._anon_root_path

    @anon_root_path.setter
    def anon_root_path(self, anon_root_path):
        """
        Sets the anon_root_path of this FtpSettingsSettings.
        This option represents a directory in /ifs which vsftpd will try to change into after an anonymous login.

        :param anon_root_path: The anon_root_path of this FtpSettingsSettings.
        :type: str
        """
        
        self._anon_root_path = anon_root_path

    @property
    def anon_umask(self):
        """
        Gets the anon_umask of this FtpSettingsSettings.
        The value that the umask for file creation is set to for anonymous users.

        :return: The anon_umask of this FtpSettingsSettings.
        :rtype: int
        """
        return self._anon_umask

    @anon_umask.setter
    def anon_umask(self, anon_umask):
        """
        Sets the anon_umask of this FtpSettingsSettings.
        The value that the umask for file creation is set to for anonymous users.

        :param anon_umask: The anon_umask of this FtpSettingsSettings.
        :type: int
        """
        
        if not anon_umask:
            raise ValueError("Invalid value for `anon_umask`, must not be `None`")
        if anon_umask > 511.0: 
            raise ValueError("Invalid value for `anon_umask`, must be a value less than or equal to `511.0`")
        if anon_umask < 0.0: 
            raise ValueError("Invalid value for `anon_umask`, must be a value greater than or equal to `0.0`")

        self._anon_umask = anon_umask

    @property
    def ascii_mode(self):
        """
        Gets the ascii_mode of this FtpSettingsSettings.
        Controls whether ascii mode data transfers are honored for various types of requests.

        :return: The ascii_mode of this FtpSettingsSettings.
        :rtype: str
        """
        return self._ascii_mode

    @ascii_mode.setter
    def ascii_mode(self, ascii_mode):
        """
        Sets the ascii_mode of this FtpSettingsSettings.
        Controls whether ascii mode data transfers are honored for various types of requests.

        :param ascii_mode: The ascii_mode of this FtpSettingsSettings.
        :type: str
        """
        allowed_values = ["off", "upload", "download", "both"]
        if ascii_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `ascii_mode`, must be one of {0}"
                .format(allowed_values)
            )

        self._ascii_mode = ascii_mode

    @property
    def chroot_exception_list(self):
        """
        Gets the chroot_exception_list of this FtpSettingsSettings.
        A list of users that are not chrooted when logging in.

        :return: The chroot_exception_list of this FtpSettingsSettings.
        :rtype: list[str]
        """
        return self._chroot_exception_list

    @chroot_exception_list.setter
    def chroot_exception_list(self, chroot_exception_list):
        """
        Sets the chroot_exception_list of this FtpSettingsSettings.
        A list of users that are not chrooted when logging in.

        :param chroot_exception_list: The chroot_exception_list of this FtpSettingsSettings.
        :type: list[str]
        """
        
        self._chroot_exception_list = chroot_exception_list

    @property
    def chroot_local_mode(self):
        """
        Gets the chroot_local_mode of this FtpSettingsSettings.
        If set to 'all', all local users will be (by default) placed in a chroot() jail in their home directory after login. If set to 'all-with-exceptions', all local users except those listed in the chroot exception list (isi ftp chroot-exception-list) will be placed in a chroot() jail in their home directory after login. If set to 'none', no local users will be chrooted by default. If set to 'none-with-exceptions', only the local users listed in the chroot exception list (isi ftp chroot-exception-list) will be place in a chroot() jail in their home directory after login.

        :return: The chroot_local_mode of this FtpSettingsSettings.
        :rtype: str
        """
        return self._chroot_local_mode

    @chroot_local_mode.setter
    def chroot_local_mode(self, chroot_local_mode):
        """
        Sets the chroot_local_mode of this FtpSettingsSettings.
        If set to 'all', all local users will be (by default) placed in a chroot() jail in their home directory after login. If set to 'all-with-exceptions', all local users except those listed in the chroot exception list (isi ftp chroot-exception-list) will be placed in a chroot() jail in their home directory after login. If set to 'none', no local users will be chrooted by default. If set to 'none-with-exceptions', only the local users listed in the chroot exception list (isi ftp chroot-exception-list) will be place in a chroot() jail in their home directory after login.

        :param chroot_local_mode: The chroot_local_mode of this FtpSettingsSettings.
        :type: str
        """
        allowed_values = ["all", "none", "all-with-exceptions", "none-with-exceptions"]
        if chroot_local_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `chroot_local_mode`, must be one of {0}"
                .format(allowed_values)
            )

        self._chroot_local_mode = chroot_local_mode

    @property
    def connect_timeout(self):
        """
        Gets the connect_timeout of this FtpSettingsSettings.
        The timeout, in seconds, for a remote client to respond to our PORT style data connection.

        :return: The connect_timeout of this FtpSettingsSettings.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """
        Sets the connect_timeout of this FtpSettingsSettings.
        The timeout, in seconds, for a remote client to respond to our PORT style data connection.

        :param connect_timeout: The connect_timeout of this FtpSettingsSettings.
        :type: int
        """
        
        if not connect_timeout:
            raise ValueError("Invalid value for `connect_timeout`, must not be `None`")
        if connect_timeout > 600.0: 
            raise ValueError("Invalid value for `connect_timeout`, must be a value less than or equal to `600.0`")
        if connect_timeout < 30.0: 
            raise ValueError("Invalid value for `connect_timeout`, must be a value greater than or equal to `30.0`")

        self._connect_timeout = connect_timeout

    @property
    def data_timeout(self):
        """
        Gets the data_timeout of this FtpSettingsSettings.
        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.

        :return: The data_timeout of this FtpSettingsSettings.
        :rtype: int
        """
        return self._data_timeout

    @data_timeout.setter
    def data_timeout(self, data_timeout):
        """
        Sets the data_timeout of this FtpSettingsSettings.
        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.

        :param data_timeout: The data_timeout of this FtpSettingsSettings.
        :type: int
        """
        
        if not data_timeout:
            raise ValueError("Invalid value for `data_timeout`, must not be `None`")
        if data_timeout > 600.0: 
            raise ValueError("Invalid value for `data_timeout`, must be a value less than or equal to `600.0`")
        if data_timeout < 30.0: 
            raise ValueError("Invalid value for `data_timeout`, must be a value greater than or equal to `30.0`")

        self._data_timeout = data_timeout

    @property
    def denied_user_list(self):
        """
        Gets the denied_user_list of this FtpSettingsSettings.
        A list of uses that will be denied access.

        :return: The denied_user_list of this FtpSettingsSettings.
        :rtype: list[str]
        """
        return self._denied_user_list

    @denied_user_list.setter
    def denied_user_list(self, denied_user_list):
        """
        Sets the denied_user_list of this FtpSettingsSettings.
        A list of uses that will be denied access.

        :param denied_user_list: The denied_user_list of this FtpSettingsSettings.
        :type: list[str]
        """
        
        self._denied_user_list = denied_user_list

    @property
    def dirlist_localtime(self):
        """
        Gets the dirlist_localtime of this FtpSettingsSettings.
        If enabled, display directory listings with the time in your local time zone. The default is to display GMT. The times returned by the MDTM FTP command are also affected by this option.

        :return: The dirlist_localtime of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._dirlist_localtime

    @dirlist_localtime.setter
    def dirlist_localtime(self, dirlist_localtime):
        """
        Sets the dirlist_localtime of this FtpSettingsSettings.
        If enabled, display directory listings with the time in your local time zone. The default is to display GMT. The times returned by the MDTM FTP command are also affected by this option.

        :param dirlist_localtime: The dirlist_localtime of this FtpSettingsSettings.
        :type: bool
        """
        
        self._dirlist_localtime = dirlist_localtime

    @property
    def dirlist_names(self):
        """
        Gets the dirlist_names of this FtpSettingsSettings.
        When set to 'hide',  all user and group information in directory listings will be displayed as 'ftp'. When set to 'textual', textual names are shown in the user and group fields of directory listings. When set to 'numeric', numeric IDs are show in the user and group fields of directory listings.

        :return: The dirlist_names of this FtpSettingsSettings.
        :rtype: str
        """
        return self._dirlist_names

    @dirlist_names.setter
    def dirlist_names(self, dirlist_names):
        """
        Sets the dirlist_names of this FtpSettingsSettings.
        When set to 'hide',  all user and group information in directory listings will be displayed as 'ftp'. When set to 'textual', textual names are shown in the user and group fields of directory listings. When set to 'numeric', numeric IDs are show in the user and group fields of directory listings.

        :param dirlist_names: The dirlist_names of this FtpSettingsSettings.
        :type: str
        """
        allowed_values = ["numeric", "textual", "hide"]
        if dirlist_names not in allowed_values:
            raise ValueError(
                "Invalid value for `dirlist_names`, must be one of {0}"
                .format(allowed_values)
            )

        self._dirlist_names = dirlist_names

    @property
    def file_create_perm(self):
        """
        Gets the file_create_perm of this FtpSettingsSettings.
        The permissions with which uploaded files are created. Umasks are applied on top of this value.

        :return: The file_create_perm of this FtpSettingsSettings.
        :rtype: int
        """
        return self._file_create_perm

    @file_create_perm.setter
    def file_create_perm(self, file_create_perm):
        """
        Sets the file_create_perm of this FtpSettingsSettings.
        The permissions with which uploaded files are created. Umasks are applied on top of this value.

        :param file_create_perm: The file_create_perm of this FtpSettingsSettings.
        :type: int
        """
        
        if not file_create_perm:
            raise ValueError("Invalid value for `file_create_perm`, must not be `None`")
        if file_create_perm > 511.0: 
            raise ValueError("Invalid value for `file_create_perm`, must be a value less than or equal to `511.0`")
        if file_create_perm < 0.0: 
            raise ValueError("Invalid value for `file_create_perm`, must be a value greater than or equal to `0.0`")

        self._file_create_perm = file_create_perm

    @property
    def limit_anon_passwords(self):
        """
        Gets the limit_anon_passwords of this FtpSettingsSettings.
        This field determines whether the anon_password_list is used.

        :return: The limit_anon_passwords of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._limit_anon_passwords

    @limit_anon_passwords.setter
    def limit_anon_passwords(self, limit_anon_passwords):
        """
        Sets the limit_anon_passwords of this FtpSettingsSettings.
        This field determines whether the anon_password_list is used.

        :param limit_anon_passwords: The limit_anon_passwords of this FtpSettingsSettings.
        :type: bool
        """
        
        self._limit_anon_passwords = limit_anon_passwords

    @property
    def local_root_path(self):
        """
        Gets the local_root_path of this FtpSettingsSettings.
        This option represents a directory in /ifs which vsftpd will try to change into after a local login.

        :return: The local_root_path of this FtpSettingsSettings.
        :rtype: str
        """
        return self._local_root_path

    @local_root_path.setter
    def local_root_path(self, local_root_path):
        """
        Sets the local_root_path of this FtpSettingsSettings.
        This option represents a directory in /ifs which vsftpd will try to change into after a local login.

        :param local_root_path: The local_root_path of this FtpSettingsSettings.
        :type: str
        """
        
        self._local_root_path = local_root_path

    @property
    def local_umask(self):
        """
        Gets the local_umask of this FtpSettingsSettings.
        The value that the umask for file creation is set to for local users.

        :return: The local_umask of this FtpSettingsSettings.
        :rtype: int
        """
        return self._local_umask

    @local_umask.setter
    def local_umask(self, local_umask):
        """
        Sets the local_umask of this FtpSettingsSettings.
        The value that the umask for file creation is set to for local users.

        :param local_umask: The local_umask of this FtpSettingsSettings.
        :type: int
        """
        
        if not local_umask:
            raise ValueError("Invalid value for `local_umask`, must not be `None`")
        if local_umask > 511.0: 
            raise ValueError("Invalid value for `local_umask`, must be a value less than or equal to `511.0`")
        if local_umask < 0.0: 
            raise ValueError("Invalid value for `local_umask`, must be a value greater than or equal to `0.0`")

        self._local_umask = local_umask

    @property
    def server_to_server(self):
        """
        Gets the server_to_server of this FtpSettingsSettings.
        If enabled, allow server-to-server (FXP) transfers.

        :return: The server_to_server of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._server_to_server

    @server_to_server.setter
    def server_to_server(self, server_to_server):
        """
        Sets the server_to_server of this FtpSettingsSettings.
        If enabled, allow server-to-server (FXP) transfers.

        :param server_to_server: The server_to_server of this FtpSettingsSettings.
        :type: bool
        """
        
        self._server_to_server = server_to_server

    @property
    def service(self):
        """
        Gets the service of this FtpSettingsSettings.
        This field controls whether the FTP daemon is running.

        :return: The service of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this FtpSettingsSettings.
        This field controls whether the FTP daemon is running.

        :param service: The service of this FtpSettingsSettings.
        :type: bool
        """
        
        self._service = service

    @property
    def session_support(self):
        """
        Gets the session_support of this FtpSettingsSettings.
        If enabled, maintain login sessions for each user through Pluggable Authentication Modules (PAM). Disabling this option prevents the ability to do automatic home directory creation if that functionality were otherwise available.

        :return: The session_support of this FtpSettingsSettings.
        :rtype: bool
        """
        return self._session_support

    @session_support.setter
    def session_support(self, session_support):
        """
        Sets the session_support of this FtpSettingsSettings.
        If enabled, maintain login sessions for each user through Pluggable Authentication Modules (PAM). Disabling this option prevents the ability to do automatic home directory creation if that functionality were otherwise available.

        :param session_support: The session_support of this FtpSettingsSettings.
        :type: bool
        """
        
        self._session_support = session_support

    @property
    def session_timeout(self):
        """
        Gets the session_timeout of this FtpSettingsSettings.
        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.

        :return: The session_timeout of this FtpSettingsSettings.
        :rtype: int
        """
        return self._session_timeout

    @session_timeout.setter
    def session_timeout(self, session_timeout):
        """
        Sets the session_timeout of this FtpSettingsSettings.
        The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off.

        :param session_timeout: The session_timeout of this FtpSettingsSettings.
        :type: int
        """
        
        if not session_timeout:
            raise ValueError("Invalid value for `session_timeout`, must not be `None`")
        if session_timeout > 600.0: 
            raise ValueError("Invalid value for `session_timeout`, must be a value less than or equal to `600.0`")
        if session_timeout < 30.0: 
            raise ValueError("Invalid value for `session_timeout`, must be a value greater than or equal to `30.0`")

        self._session_timeout = session_timeout

    @property
    def user_config_dir(self):
        """
        Gets the user_config_dir of this FtpSettingsSettings.
        Specifies the directory where per-user config overrides can be found.

        :return: The user_config_dir of this FtpSettingsSettings.
        :rtype: str
        """
        return self._user_config_dir

    @user_config_dir.setter
    def user_config_dir(self, user_config_dir):
        """
        Sets the user_config_dir of this FtpSettingsSettings.
        Specifies the directory where per-user config overrides can be found.

        :param user_config_dir: The user_config_dir of this FtpSettingsSettings.
        :type: str
        """
        
        self._user_config_dir = user_config_dir

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

