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

import rsd_lib

from rsdclient.v1 import node
from rsdclient.v1 import storage


class Client(object):

    def __init__(self, base_url, username, password, verify=True):
        self.client = rsd_lib.RSDLib(base_url, username, password,
                                     verify=verify)
        self.node = node.NodeManager(self.client)
        self.storage = storage.StorageManager(self.client)
