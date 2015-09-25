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

""" Utilities and helper functions """
import configparser
import dnf
import io
import requests
from lib import settings

def _url_as_ini_file(url):
    """
    Returns a file-like object of an URL to use it with configparser
    """
    text = requests.get(url).text
    inifile = io.StringIO(text)
    inifile.seek(0)
    return inifile


def fetch_base_urls(version):
    """
    Parses a ini-like repo file and returns the base urls
    """
    repo_config = _url_as_ini_file(settings.RELEASES[version]['url'])
    config = configparser.SafeConfigParser()
    config.readfp(repo_config)

    base_urls = list()
    for repository in config.sections():
        base_urls.append((config.get(repository, 'name'),
                          config.get(repository, 'baseurl')))

    return base_urls


def get_packages_from_repo(version):
    """
    Uses the dnf API to fetch the list of all available packages off of a baseurl
    """
    base = dnf.Base()
    base_urls = fetch_base_urls(version)
    for name, base_url in base_urls:
        repo = dnf.repo.Repo(name, settings.TMPDIR)
        repo.baseurl = [base_url]
        base.repos.add(repo)
    base.fill_sack()

    # A query matches all packages in sack
    q = base.sack.query()
    # Derived query matches only available packages
    q_avail = q.available()
    packages = q_avail.run()

    return packages