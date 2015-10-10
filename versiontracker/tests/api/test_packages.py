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

import io
import mock
import unittest

from versiontracker.tests import fakes
from versiontracker.api.packages import _fetch_base_urls


@mock.patch('versiontracker.api.packages._url_as_ini_file')
class TestFetchBaseUrls(unittest.TestCase):
    def test_parse_repo_file_with_one_repo(self, _url_mock):
        fake_inifile = io.StringIO(fakes.REPO_CONFIG_ONE)
        fake_inifile.seek(0)
        _url_mock.return_value = fake_inifile
        expected_base_url = [('repo-one',
                             'http://example.org/one/x86_64/packages')]
        base_url = _fetch_base_urls('repo-one')
        self.assertEquals(expected_base_url, base_url)

    def test_parse_repo_file_with_n_repo(self, _url_mock):
        fake_inifile = io.StringIO(fakes.TWO_REPO_CONFIGS)
        fake_inifile.seek(0)
        _url_mock.return_value = fake_inifile
        expected_base_url = [('repo-one',
                             'http://example.org/one/x86_64/packages'),
                             ('repo-two',
                             'http://example.org/two/x86_64/packages')]
        base_url = _fetch_base_urls('two-repo-configs')
        self.assertEquals(expected_base_url, base_url)
