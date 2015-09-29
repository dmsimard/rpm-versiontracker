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


class Repositories(Resource):
    def get(self, repository=None, param=None):
        if repository:
            if param:
                try:
                    return settings.REPOSITORIES[repository][param]
                except KeyError as e:
                    raise KeyError("{0} is not configured in {1}: {2}".format(param, repository, repr(e)))
            try:
                return settings.REPOSITORIES[repository]
            except KeyError as e:
                raise KeyError("{0} is not configured: {1}".format(repository, repr(e)))
        return settings.REPOSITORIES


class Tags(Resource):
    def get(self, tag=None, param=None):
        if tag:
            if param:
                try:
                    return settings.TAGS[tag][param]
                except KeyError as e:
                    raise KeyError("{0} is not configured in {1}: {2}".format(param, tag, repr(e)))
            try:
                return settings.TAGS[tag]
            except KeyError as e:
                raise KeyError("{0} is not configured: {1}".format(tag, repr(e)))
        return settings.TAGS


class PackageProperties(Resource):
    def get(self):
        return settings.PACKAGE_PROPERTIES
