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

"""
Default settings showing versions of packages provided for two releases of Openstack.
You can override these settings with the local_settings.py file.
"""

import collections
import os

# Where DNF cache data will be stored
TMPDIR = '/tmp/'

# So we can know where we're loaded from
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# An ordered dict is recommended to have a consistent display experience but is not required.
# Adding a repository in the following format will make it available in the top menu automatically.
REPOSITORIES = collections.OrderedDict({
    'liberty-master': {
        'name': 'liberty-master',
        'friendly_name': 'Liberty (master)',
        'url':  'http://trunk.rdoproject.org/centos7-liberty/current/delorean.repo'
    },
    'liberty-master-ci': {
        'name': 'liberty-master-ci',
        'friendly_name': 'Liberty (CI tested)',
        'url':  'http://trunk.rdoproject.org/centos7-liberty/current-passed-ci/delorean.repo'
    },
    'kilo-master': {
        'name': 'kilo-master',
        'friendly_name': 'Kilo (master)',
        'url': 'http://trunk.rdoproject.org/centos7-kilo/current/delorean-kilo.repo'
    },
    'kilo-master-ci': {
        'name': 'kilo-master-ci',
        'friendly_name': 'Kilo (CI tested)',
        'url': 'http://trunk.rdoproject.org/centos7-kilo/current-passed-ci/delorean-kilo.repo'
    }
})

# An ordered dict is recommended to have a consistent display experience but is not required.
# Adding a tag in the following format will make it available in the compare menu automatically.
# A tag has to match at least two repositories to be useful.
TAGS = collections.OrderedDict({
    'liberty': {
        'name': 'liberty',
        'friendly_name': 'Liberty repositories'
    },
    'kilo': {
        'name': 'kilo',
        'friendly_name': 'Kilo repositories'
    }
})

# http://dnf.readthedocs.org/en/latest/api_package.html
PACKAGE_PROPERTIES = ['arch', 'buildtime', 'downloadsize', 'epoch', 'files', 'installtime', 'installsize', 'name',
                  'release', 'sourcerpm', 'version']

if os.path.exists(os.path.join(BASE_DIR, 'local_settings.py')):
    from versiontracker.local_settings import *