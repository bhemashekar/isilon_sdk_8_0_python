# coding: utf-8

"""
SyncPoliciesApi.py
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
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SyncPoliciesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_policy_reset_item(self, policy_reset_item, policy, **kwargs):
        """
        
        Reset a SyncIQ policy incremental state and force a full sync/copy.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_policy_reset_item(policy_reset_item, policy, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Empty policy_reset_item:  (required)
        :param str policy:  (required)
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['policy_reset_item', 'policy']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_policy_reset_item" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'policy_reset_item' is set
        if ('policy_reset_item' not in params) or (params['policy_reset_item'] is None):
            raise ValueError("Missing the required parameter `policy_reset_item` when calling `create_policy_reset_item`")
        # verify the required parameter 'policy' is set
        if ('policy' not in params) or (params['policy'] is None):
            raise ValueError("Missing the required parameter `policy` when calling `create_policy_reset_item`")


        resource_path = '/platform/1/sync/policies/{Policy}/reset'.replace('{format}', 'json')
        path_params = {}
        if 'policy' in params:
            path_params['Policy'] = params['policy']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'policy_reset_item' in params:
            body_params = params['policy_reset_item']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['basic_auth']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='CreateResponse',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
