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
This is where you would override the default settings as configured in settings.py
"""

import collections
import os

# Where DNF cache data will be stored
# TMPDIR = '/tmp/'

# So we can know where we're loaded from
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# An ordered dict is recommended to have a consistent display experience but is not required.
# Adding a release in the following format will make it available in the top menu automatically.
# RELEASES = collections.OrderedDict({
#    'liberty-master': {
#        'name': 'liberty-master',
#        'friendly_name': 'Liberty (master)',
#        'url':  'http://trunk.rdoproject.org/centos7-liberty/current/delorean.repo'
#    },
#    'liberty-master-ci': {
#        'name': 'liberty-master-ci',
#        'friendly_name': 'Liberty (CI tested)',
#        'url':  'http://trunk.rdoproject.org/centos7-liberty/current-passed-ci/delorean.repo'
#    },
#    'kilo-master': {
#        'name': 'kilo-master',
#        'friendly_name': 'Kilo (master)',
#        'url': 'http://trunk.rdoproject.org/centos7-kilo/current/delorean-kilo.repo'
#    },
#    'kilo-master-ci': {
#        'name': 'kilo-master-ci',
#        'friendly_name': 'Kilo (CI tested)',
#        'url': 'http://trunk.rdoproject.org/centos7-kilo/current-passed-ci/delorean-kilo.repo'
#    }
# })

# An ordered dict is recommended to have a consistent display experience but is not required.
# Adding a tag in the following format will make it available in the compare menu automatically.
# A tag has to match at least two releases to be useful.
# TAGS = collections.OrderedDict({
#     'liberty': {
#         'name': 'liberty',
#         'friendly_name': 'Liberty releases'
#     },
#     'kilo': {
#         'name': 'kilo',
#         'friendly_name': 'Kilo releases'
#     }
# })