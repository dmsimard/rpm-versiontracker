``rpm-versiontracker`` is a small, generic, [Flask](http://flask.pocoo.org/)
web application that leverages the
[DNF API](http://dnf.readthedocs.org/en/latest/index.html) to display the list
 of packages available from different repositories and compare them.

It provides a REST API to query it’s settings and return package lists so you
can build and integrate around it.

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

Documentation
=============
Documentation on the REST API, how to install, configure and run
``rpm-versiontracker`` is available on
[ReadTheDocs.org](http://rpm-versiontracker.readthedocs.org/en/latest/)

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
