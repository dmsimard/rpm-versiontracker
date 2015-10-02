#   Copyright Red Hat, Inc. All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import collections

REPO_CONFIG_ONE = """
[repo-one]
name=repo-one
baseurl=http://example.org/one/x86_64/packages
enabled=1
gpgcheck=0
priority=1
"""

REPO_CONFIG_TWO = """
[repo-two]
name=repo-two
baseurl=http://example.org/two/x86_64/packages
enabled=1
gpgcheck=0
priority=1
"""

TWO_REPO_CONFIGS = REPO_CONFIG_ONE + REPO_CONFIG_TWO

class FakeSettings(object):
    def __init__(self):
        self.REPOSITORIES = collections.OrderedDict({
            'repo-one': {
                'name': 'repo-one',
                'friendly_name': 'Repo One',
                'url':  'http://example.org/one/x86_64.repo'
            },
            'repo-two': {
                'name': 'repo-two',
                'friendly_name': 'Repo Two',
                'url':  'http://example.org/two/x86_64.repo'
            }
        })
        self.TAGS = collections.OrderedDict({
            'repo': {
                'name': 'repo',
                'friendly_name': 'Repositories'
            }
        })
        self.PACKAGE_PROPERTIES = ['arch', 'buildtime', 'name', 'release',
                                   'version']

        self.TMP_DIR = '/tmp/'


class FakePackageOne(object):
    def __init__(self):
        self.arch = 'x86_64'
        self.buildtime = 946684800
        self.name = 'fake-package-one'
        self.release = 'foo'
        self.version = '0.1'


class FakeDifferentPackageOne(object):
    def __init__(self):
        self.arch = 'x86_64'
        self.buildtime = 946684800
        self.name = 'fake-package-one'
        self.release = 'foo'
        self.version = '1.0'


class FakePackageTwo(object):
    def __init__(self):
        self.arch = 'x86_64'
        self.buildtime = 946684800
        self.name = 'fake-package-two'
        self.release = 'foo'
        self.version = '0.2'


class FakePackageThree(object):
    def __init__(self):
        self.arch = 'x86_64'
        self.buildtime = 946684800
        self.name = 'fake-package-three'
        self.release = 'foo'
        self.version = '3.0'
