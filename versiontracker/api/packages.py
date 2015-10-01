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
import configparser
import dnf
import io
import requests
from flask_restful import Resource

from versiontracker import settings


class Packages(Resource):
    def get(self, repository, package=None, property=None):
        packages = collections.OrderedDict()
        try:
            repository_packages = _get_packages_from_repo(repository)
        except KeyError as e:
            msg = "{0} is not configured: {1}".format(repository, repr(e))
            raise KeyError(msg)

        for repository_package in repository_packages:
            package_index = "{0}-{1}".format(repository_package.name,
                                             repository_package.arch)
            packages[package_index] = {}
            for pkg_property in settings.PACKAGE_PROPERTIES:
                packages[package_index][pkg_property] = \
                    getattr(repository_package, pkg_property)

        if package:
            if property:
                try:
                    return packages[package][property]
                except KeyError as e:
                    msg = "{0} is not available in {1}: {2}".format(property,
                                                                    package,
                                                                    repr(e))
                    raise KeyError(msg)

            try:
                return packages[package]
            except KeyError as e:
                msg = "{0} is not in the list of packages: {1}".format(package,
                                                                       repr(e))
                raise KeyError(msg)

        return packages


def _fetch_base_urls(repository):
    """
    Parses a ini-like repo file and returns the base urls
    """
    repo_config = _url_as_ini_file(settings.REPOSITORIES[repository]['url'])
    config = configparser.ConfigParser()
    config.read_file(repo_config)

    base_urls = list()
    for repo in config.sections():
        base_urls.append((config.get(repo, 'name'),
                          config.get(repo, 'baseurl')))

    return base_urls


def _get_packages_from_repo(repository):
    """
    Uses the dnf API to fetch the list of all available packages from a baseurl
    """
    base = dnf.Base()
    base_urls = _fetch_base_urls(repository)
    for name, base_url in base_urls:
        repo = dnf.repo.Repo(name, settings.TMPDIR)
        repo.baseurl = [base_url]
        base.repos.add(repo)
    base.fill_sack()

    # Query all available packages in sack
    packages = base.sack.query().available().run()

    return packages


def _url_as_ini_file(url):
    """
    Returns a file-like object of an URL to use it with configparser
    """
    text = requests.get(url).text
    inifile = io.StringIO(text)
    inifile.seek(0)
    return inifile
