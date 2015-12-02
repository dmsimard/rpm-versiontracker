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
import collections

from versiontracker import settings
from versiontracker.api.packages import Packages


def diff_packages(repositories):
    """
    Iterates over a list of packages dictionaries and highlights differences,
    if any. Returns the same dictionary with an extra key to show if there are
    differences.

    Creates common keys for packages such as arch, package name and different.
    """
    # TODO: I don't like this part, it works but needs improvement.
    # Retrieve packages for each repository
    packages = collections.OrderedDict()
    for repository in repositories:
        repository_packages = Packages().get(repository)
        for package in repository_packages:
            if package not in packages:
                packages[package] = collections.defaultdict(dict)
            for property in settings.PACKAGE_PROPERTIES:
                value = repository_packages[package][property]
                packages[package][repository][property] = value

    # Highlight package differences, if any
    for package in packages:
        compare_version = ""
        packages[package]['different'] = False
        for repository in repositories:
            try:
                name = packages[package][repository]['name']
                arch = packages[package][repository]['arch']
                version = packages[package][repository]['version']
                release = packages[package][repository]['release']
            except KeyError:
                pass
            try:
                # Set common keys if they haven't been set up yet.
                if not packages[package]['arch']:
                    packages[package]['name'] = name
                    packages[package]['arch'] = arch
            except KeyError:
                pass
            try:
                full_version = version + release
            except KeyError:
                # Package exists in at least one repository and doesn't exist
                # in at least one repository.
                packages[package]['different'] = True
            if not compare_version:
                # Establish a base for comparison
                compare_version = full_version
            if compare_version == full_version:
                # Version for this repository is identical to the last one
                # compared against.
                continue
            else:
                # Version for this repository is not identical to the last one
                # compared against
                packages[package]['different'] = True

    return packages
