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
import datetime
from flask import Flask, render_template
from flask_restful import Api

from versiontracker import utils
from versiontracker import settings

from versiontracker.api.repositories import Repositories
from versiontracker.api.packages import Packages

app = Flask(__name__)
api = Api(app)
api.add_resource(Repositories,
                 '/repositories',
                 '/repositories/<string:repository>',
                 '/repositories/<string:repository>/<string:param>')

api.add_resource(Packages,
                 '/packages/<string:repository>',
                 '/packages/<string:repository>/<string:package>',
                 '/packages/<string:repository>/<string:package>/<string:param>')


# Jinja Filters
@app.template_filter('datetime')
def jinja_date_formatter(timestamp, format='%Y-%m-%d %H:%M:%S'):
    """ Formats a unix timestamp """
    return datetime.datetime.fromtimestamp(timestamp).strftime(format)


@app.template_filter('truncate')
def jinja_truncate_string(string, length=40):
    """ Truncates a string to max length """
    return string[:length] + (string[length:] and '...')


# App routing
@app.route('/')
def main():
    return render_template('home.html', repositories=settings.REPOSITORIES,
                           tags=settings.TAGS)


@app.route('/details/<repository>')
def details(repository):
    """ Returns the list of packages for <repository> """
    packages = utils.get_packages_from_repo(repository)
    return render_template('details.html', repositories=settings.REPOSITORIES,
                           tags=settings.TAGS, repository=repository,
                           packages=packages)


@app.route('/compare/<tag>')
def compare(tag):
    """ Compares the versions across different repositories matching <tag> """
    # TODO: I don't like this part, it works but needs improvement. Move to a function ?
    # Retrieve 'params' of each package of each release
    packages = collections.OrderedDict()
    for repository in settings.REPOSITORIES:
        if tag in repository:
            repository_packages = utils.get_packages_from_repo(repository)
            for package in repository_packages:
                if package.name not in packages:
                    packages[package.name] = collections.defaultdict(dict)
                for param in settings.PACKAGE_PARAMS:
                    packages[package.name][repository][param] = getattr(package, param)

    # Match package versions for each release to highlight differences
    packages = utils.diff_packages(packages, tag)

    return render_template('compare.html', repositories=settings.REPOSITORIES,
                           tags=settings.TAGS, tag=tag, packages=packages)

