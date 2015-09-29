Running
=======
Quickstart: Standalone
~~~~~~~~~~~~~~~~~~~~~~
Flask_ provides a built-in webserver and it is sufficient for self hosting
``rpm-versiontracker`` and personal usage.

To start the standalone webserver::

    $ ./run.py
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

You will be able to access the application on http://127.0.0.1:5000/.

.. _Flask: http://flask.pocoo.org/

Running behind an application and web server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you are expecting any kind of real traffic, you probably want to run
``rpm-versiontracker`` from an application server and put a web server or
reverse-proxy in front of it.

There's many ways to get a Flask application running. Flask has great
documentation_ on the different deployment options.

Perhaps your favorite setup is with `Apache and mod_wsgi`_ or you're used to
`gunicorn`_ and nginx_ in front instead. Flask is very flexible in this regard.

What you need to know is that the application to start is ``run:app`` where
``run`` references `run.py`_ and ``app`` the actual Flask application.

The REST API is currently unrestricted. It is highly recommended to secure
access to it with the help of a web server or other means as it could fairly
easily be abused or used in amplification attacks.

.. _documentation: http://flask.pocoo.org/docs/0.10/deploying/
.. _Apache and mod_wsgi: http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/
.. _gunicorn: http://flask.pocoo.org/docs/0.10/deploying/wsgi-standalone/#gunicorn
.. _nginx: http://nginx.org/
.. _run.py: https://github.com/dmsimard/rpm-versiontracker/blob/master/run.py
