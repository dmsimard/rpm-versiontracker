Configuring
===========
``rpm-versiontracker`` ships with a default configuration that shows different
Openstack repositories.

You can override the default configuration by editing the `local_settings.py`_
file.

.. _local_settings.py: https://github.com/dmsimard/rpm-versiontracker/blob/master/local_settings.py

Settings
~~~~~~~~
* ``TMPDIR`` is a path that defines where ``DNF`` will store it's repository
  cache.
* ``REPOSITORIES`` defines which repositories can be queried and has the
  following structure. Configured repositories will automatically show up in the
  top menu.
* ``TAGS`` is a string matcher. It will automatically create a link in the
  ``Compare`` tab of the top menu for comparing repositories that match the tag
  string.
* ``PACKAGE_PROPERTIES`` defines which properties are pulled from DNF and made
  available through the API. The interface does not display all package
  properties in the detailed and comparison tables.
* ``SHOW_SOURCE_RPM`` is a toggle to display (or not) the source RPM packages
  alongside the various architecture packages.

Read on the `running documentation`_ to see how to get ``rpm-versiontracker``
to run.

.. _running documentation: running.html