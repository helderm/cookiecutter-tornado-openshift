======================
cookiecutter-tornado-openshift
======================

Cookiecutter_ template for a Openshift application using Tornado asynchronous libraries and the DIY cartridge.

* GitHub repo: https://github.com/helderm/cookiecutter-tornado-openshift/
* Free software: BSD license

Features
--------

* Action hooks for starting, stopping and building the app in a self contained virtualenv in Openshift
* Async testing using tornado.testing module
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4, 3.5
* Dev virtualenv creation with `tox -e devenv`

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Quickstart
----------

Generate a Python package project::

    cookiecutter https://github.com/helderm/cookiecutter-tornado-openshift.git

Then:

* Create a repo and put it there.
* Create a dev virtualenv with `tox -e devenv`
* Activate your virtualenv with `source devenv/{app_name}/bin/activate
* Run the server with `python {app_name}/{app_name}.py`
* Test it by running `curl -v "localhost:8080"`

.. _Tox: http://testrun.org/tox/
