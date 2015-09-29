REST API
========
``rpm-versiontracker`` provides a REST API in order to build and integrate
around it.

The REST API is currently unrestricted. It is highly recommended to secure
access to it with the help of a web server or other means as it could fairly
easily be abused or used in amplification attacks.

Settings
........
Repositories
~~~~~~~~~~~~
.. http:get:: /settings/repositories/(str:repository)/(str:param)

    Retrieve all repositories and their properties or,
    a repository and it's properties or,
    a specific property from a repository

Retrieve all repositories and their properties
----------------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/repositories HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      {
        "liberty-master": {
          "url": "http:\/\/trunk.rdoproject.org\/centos7-liberty\/current\/delorean.repo",
          "name": "liberty-master",
          "friendly_name": "Liberty (master)"
        },
        "kilo-master": {
          "url": "http:\/\/trunk.rdoproject.org\/centos7-kilo\/current\/delorean-kilo.repo",
          "name": "kilo-master",
          "friendly_name": "Kilo (master)"
        }
      }


Retrieve the properties of a single repository
----------------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/repositories/liberty-master HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      {
        "url": "http:\/\/trunk.rdoproject.org\/centos7-liberty\/current\/delorean.repo",
        "name": "liberty-master",
        "friendly_name": "Liberty (master)"
      }

Retrieve a specific property from a single repository
-----------------------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/repositories/liberty-master/url HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      "http://trunk.rdoproject.org/centos7-liberty/current/delorean.repo"

Tags
~~~~
.. http:get:: /settings/tags/(str:tag)/(str:param)

    Retrieve all tags and their properties or,
    a tag and it's properties or,
    a specific property from a tag

Retrieve all tags and their properties
--------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/tags HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      {
        "kilo": {
          "name": "kilo",
          "friendly_name": "Kilo repositories"
        },
        "liberty": {
          "name": "liberty",
          "friendly_name": "Liberty repositories"
        }
      }


Retrieve the properties of a single tag
---------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/tags/liberty HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      {
        "name": "liberty",
        "friendly_name": "Liberty repositories"
      }

Retrieve a specific property from a single tag
----------------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/tags/liberty/friendly_name HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      "Liberty repositories"

Package Properties
~~~~~~~~~~~~~~~~~~
.. http:get:: /settings/packageproperties

    Returns the list of properties that is pulled from DNF and made available
    through the API when retrieving packages.

Retrieve the list of properties pulled from DNF
-----------------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/packageproperties HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      [
        "arch",
        "buildtime",
        "downloadsize",
        "epoch",
        "files",
        "installtime",
        "installsize",
        "name",
        "release",
        "sourcerpm",
        "version"
      ]

Showing source packages
~~~~~~~~~~~~~~~~~~~~~~~
.. http:get:: /settings/showsourcerpm

    Returns ``true`` or ``false`` to show or hide source packages, respectively.
    Note: This setting only impacts the web interface for the time being.

Retrieve the setting to know if source RPMs are hidden
------------------------------------------------------
   **Example request**:

   .. sourcecode:: http

      GET /settings/showsourcerpm HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      false

Packages
........
.. http:get:: /packages/(str:repository)/(str:package)/(str:property)

    Retrieve all packages and their properties from a specified repository or,
    a package and it's properties or,
    a specific property from a package

Retrieve all packages and their properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   **Example request**:

   .. sourcecode:: http

      GET /packages/liberty-master HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      {
        "python-saharaclient": {
          "arch": "src",
          "sourcerpm": null,
          "release": "dev22.el7.centos",
          "version": "0.11.1",
          "name": "python-saharaclient",
          "buildtime": 1443451578
        },
        "python-glanceclient": {
          "arch": "src",
          "sourcerpm": null,
          "release": "dev10.el7.centos",
          "version": "1.1.1",
          "name": "python-glanceclient",
          "buildtime": 1443441984
        },
        "python-keystone": {
          "arch": "noarch",
          "sourcerpm": "openstack-keystone-9.0.0-dev27.el7.centos.src.rpm",
          "release": "dev27.el7.centos",
          "version": "9.0.0",
          "name": "python-keystone",
          "buildtime": 1443474407
        },
        [...]
      }


Retrieve the properties of a single package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   **Example request**:

   .. sourcecode:: http

      GET /packages/liberty-master/python-keystone HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      {
        "arch": "noarch",
        "sourcerpm": "openstack-keystone-9.0.0-dev27.el7.centos.src.rpm",
        "release": "dev27.el7.centos",
        "version": "9.0.0",
        "name": "python-keystone",
        "buildtime": 1443474407
      }

Retrieve a specific property from a single package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   **Example request**:

   .. sourcecode:: http

      GET /packages/liberty-master/python-keystone/sourcerpm HTTP/1.1
      Host: example.org
      Accept: application/json

   **Example response**:

   .. sourcecode:: http

      HTTP/1.0 200 OK
      Content-Type: application/json

      "openstack-keystone-9.0.0-dev27.el7.centos.src.rpm"
