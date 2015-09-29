rpm-versiontracker is a small, generic, [Flask](http://flask.pocoo.org/) web
application that leverages the
[DNF API](http://dnf.readthedocs.org/en/latest/index.html) to display the list
 of packages available from different repositories and compare them.

``DNF`` is short for ``Dandified Yum``, the next generation of package
management for Red Hat based distributions.

Use case
========
The typical use case for this application is to monitor which version is in
which repository.

If you happen to have multiple mirrors for your packages (_ex: trunk, staging,
production_), this tool could be useful.

We have created this application to be able to easily distinguish versions of
the same packages across different repositories.

What it looks like
==================
This application is currently used for following package versions across
different Openstack repositories [here](http://versiontracker.dmsimard.com).

Installing
==========
Dependencies
------------
__CentOS 7/RHEL7__:

    yum install dnf python34 python3-pip
    pip3 install -r requirements.txt

__Fedora 22+__:

    dnf install python3 python3-pip
    pip3 install -r requirements.txt

Configuration
-------------
Set up your repositories and tags in
[local_settings.py](local_settings.py).

Making the application available
--------------------------------
Flask provides a standalone web server but it is recommended to use a proper
application server and put a proxy in front of it.

You can refer to the
[Flask documentation](http://flask.pocoo.org/docs/0.10/deploying/) for
instructions on how to set this up but essentially:

- Set up an application server (_wsgi, uwsgi, gunicorn, etc._) to use
 ``versiontracker:app``.
- Set up a proxy in front your application server (_apache, nginx, etc._)

Otherwise, you can just execute ``versiontracker.py`` and it'll fire a version
of the application locally on http://127.0.0.1:5000.

Author
======
David Moreau Simard

Copyright
=========
Copyright 2015 Red Hat, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
