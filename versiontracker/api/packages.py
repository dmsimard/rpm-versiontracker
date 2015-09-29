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

from flask_restful import Resource

from versiontracker import settings
from versiontracker import utils


class Packages(Resource):
    def get(self, repository, package=None, property=None):
        packages = {}
        try:
            repository_packages = utils.get_packages_from_repo(repository)
        except KeyError as e:
            return "{0} repository is not configured: {1}".format(repository, repr(e))

        for repository_package in repository_packages:
            packages[repository_package.name] = {}
            for property in settings.PACKAGE_PROPERTIES:
                packages[repository_package.name][property] = getattr(repository_package, property)

        if package:
            if property:
                try:
                    return packages[package][property]
                except KeyError as e:
                    return "{0} for {1} is not in the list of packages: {2}".format(property, packages, repr(e))

            try:
                return packages[package]
            except KeyError as e:
                return "{0} is not in the list of packages: {1}".format(package, repr(e))

        return packages
