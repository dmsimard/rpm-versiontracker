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

import datetime
from flask import Flask, render_template
from flask_restful import Api

from versiontracker import utils

from versiontracker.api.packages import Packages
from versiontracker.api.settings import Repositories
from versiontracker.api.settings import Tags, PackageProperties, ShowSourceRpm

app = Flask(__name__)
api = Api(app)

api.add_resource(Packages,
                 '/packages/<string:repository>',
                 '/packages/<string:repository>/<string:package>',
                 '/packages/<string:repository>/<string:package>/'
                 '<string:property>')
api.add_resource(Repositories,
                 '/settings/repositories',
                 '/settings/repositories/<string:repository>',
                 '/settings/repositories/<string:repository>/<string:param>')
api.add_resource(Tags,
                 '/settings/tags',
                 '/settings/tags/<string:tag>',
                 '/settings/tags/<string:tag>/<string:param>')
api.add_resource(PackageProperties,
                 '/settings/packageproperties')
api.add_resource(ShowSourceRpm,
                 '/settings/showsourcerpm')


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
# Common/default settings
repositories = Repositories().get()
tags = Tags().get()
show_source_rpm = ShowSourceRpm().get()
default_settings = {
    'repositories': repositories,
    'tags': tags,
    'show_source_rpm': show_source_rpm
}


@app.route('/')
def main():
    """ Returns the home page """
    return render_template('home.html', **default_settings)


@app.route('/details/<repository>')
def details(repository):
    """ Returns the list of packages for <repository> """
    packages = Packages().get(repository=repository)
    return render_template('details.html', repository=repository,
                           packages=packages, **default_settings)


@app.route('/compare/<tag>')
def compare(tag):
    """ Compares the versions across different repositories matching <tag> """
    matched_repositories = [repository for repository in repositories
                            if tag in repository]

    # Match package versions for each release to highlight differences
    packages = utils.diff_packages(matched_repositories)

    return render_template('compare.html', tag=tag, packages=packages,
                           **default_settings)

if __name__ == '__main__':
    app.run()
