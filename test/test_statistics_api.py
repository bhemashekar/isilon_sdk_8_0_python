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

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.statistics_api import StatisticsApi


class TestStatisticsApi(unittest.TestCase):
    """ StatisticsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.statistics_api.StatisticsApi()

    def tearDown(self):
        pass

    def test_get_statistics_current(self):
        """
        Test case for get_statistics_current

        
        """
        pass

    def test_get_statistics_history(self):
        """
        Test case for get_statistics_history

        
        """
        pass

    def test_get_statistics_key(self):
        """
        Test case for get_statistics_key

        
        """
        pass

    def test_get_statistics_keys(self):
        """
        Test case for get_statistics_keys

        
        """
        pass

    def test_get_statistics_operations(self):
        """
        Test case for get_statistics_operations

        
        """
        pass

    def test_get_statistics_protocols(self):
        """
        Test case for get_statistics_protocols

        
        """
        pass

    def test_get_summary_client(self):
        """
        Test case for get_summary_client

        
        """
        pass

    def test_get_summary_drive(self):
        """
        Test case for get_summary_drive

        
        """
        pass

    def test_get_summary_heat(self):
        """
        Test case for get_summary_heat

        
        """
        pass

    def test_get_summary_protocol(self):
        """
        Test case for get_summary_protocol

        
        """
        pass

    def test_get_summary_system(self):
        """
        Test case for get_summary_system

        
        """
        pass


if __name__ == '__main__':
    unittest.main()