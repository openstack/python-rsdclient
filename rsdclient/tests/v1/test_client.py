#   Copyright 2017 Intel, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#

import mock
import testtools

from rsdclient.v1 import client


class ClientInitializeTest(testtools.TestCase):

    @mock.patch('sushy.Sushy')
    def test_init_client(self, mock_sushy):
        client.Client('fake_rsd_url', 'fake_username', 'fake_password')
        mock_sushy.assert_called_once_with('fake_rsd_url', 'fake_username',
                                           'fake_password', verify=True)
        client.Client('fake_rsd_url', 'fake_username', 'fake_password',
                      verify=False)
        mock_sushy.assert_called_with('fake_rsd_url', 'fake_username',
                                      'fake_password', verify=False)
