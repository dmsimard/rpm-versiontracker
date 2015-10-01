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
    def get(self, repository=None, property=None):
        if repository:
            if property:
                try:
                    return settings.REPOSITORIES[repository][property]
                except KeyError as e:
                    msg = "{0} is not configured in {1}: {2}".format(property,
                                                                     repository,
                                                                     repr(e))
                    raise KeyError(msg)
            try:
                return settings.REPOSITORIES[repository]
            except KeyError as e:
                msg = "{0} is not configured: {1}".format(repository, repr(e))
                raise KeyError(msg)
        return settings.REPOSITORIES


class Tags(Resource):
    def get(self, tag=None, property=None):
        if tag:
            if property:
                try:
                    return settings.TAGS[tag][property]
                except KeyError as e:
                    msg = "{0} is not configured in {1}: {2}".format(property,
                                                                     tag,
                                                                     repr(e))
                    raise KeyError(msg)
            try:
                return settings.TAGS[tag]
            except KeyError as e:
                msg = "{0} is not configured: {1}".format(tag, repr(e))
                raise KeyError(msg)
        return settings.TAGS


class PackageProperties(Resource):
    def get(self):
        return settings.PACKAGE_PROPERTIES


class ShowSourceRpm(Resource):
    def get(self):
        return settings.SHOW_SOURCE_RPM
