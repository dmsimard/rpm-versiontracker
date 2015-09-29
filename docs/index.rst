Welcome to rpm-versiontracker's documentation!
==============================================

rpm-versiontracker_ is a small, generic, Flask_ web application that
leverages the `DNF API`_ to display the list of packages available from
different repositories and compare them.

It provides a REST API to query it's settings and return package lists so you
can build and integrate around it.

``DNF`` is short for ``Dandified Yum``, the next generation of package
management for Red Hat based distributions.

.. _rpm-versiontracker: https://github.com/dmsimard/rpm-versiontracker
.. _Flask: http://flask.pocoo.org/
.. _DNF API: http://dnf.readthedocs.org/en/latest/index.html

Table of Contents
=================

.. toctree::
    :maxdepth: 2

    Installing <installing>
    Configuring <configuring>
    Running <running>
    REST API <api>
