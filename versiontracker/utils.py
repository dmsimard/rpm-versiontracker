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

from versiontracker import settings


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
    repo_config = _url_as_ini_file(settings.REPOSITORIES[version]['url'])
    config = configparser.ConfigParser()
    config.read_file(repo_config)

    base_urls = list()
    for repository in config.sections():
        base_urls.append((config.get(repository, 'name'),
                          config.get(repository, 'baseurl')))

    return base_urls


def get_packages_from_repo(repository):
    """
    Uses the dnf API to fetch the list of all available packages off of a baseurl
    """
    base = dnf.Base()
    base_urls = fetch_base_urls(repository)
    for name, base_url in base_urls:
        repo = dnf.repo.Repo(name, settings.TMPDIR)
        repo.baseurl = [base_url]
        base.repos.add(repo)
    base.fill_sack()

    # Query all available packages in sack
    packages = base.sack.query().available().run()

    return packages

def diff_packages(packages, tag):
    """
    Iterates over a list of packages dictionaries and highlights differences, if any.
    Returns the same dictionary with an extra key to show if there are differences.
    """
    # TODO: I don't like this part, it works but needs improvement.
    # Highlight package differences, if any
    for package in packages:
        compare_version = ""
        packages[package]['different'] = False
        for repository in settings.REPOSITORIES:
            if tag in repository:
                try:
                    full_version = packages[package][repository]['version'] + packages[package][repository]['release']
                except KeyError:
                    # Package exists in at least one repository and doesn't exist in at least one repository
                    packages[package]['different'] = True
                if not compare_version:
                    # Establish a base for comparison
                    compare_version = full_version
                if compare_version == full_version:
                    # Version for this repository is identical to the last one compared against
                    continue
                else:
                    # Version for this repository is not identical to the last one compared against
                    packages[package]['different'] = True

    return packages