======================
cookiecutter-pypackage
======================

Cookiecutter template for a Python package. See https://github.com/audreyr/cookiecutter.

* Free software: BSD license
* Vanilla testing setup with `unittest` and `python setup.py test`
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.7 and 3.4
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_

About
-----

This template is forked from audreyr's version and features these changes:

* `tests` directory is moved inside of the Python Package.
* Tox tests use Python 2.7 and 3.4 (2.6 and 3.3 were removed).
* Various files have small formatting changes (e.g. `AUTHORS.rst`).
* Python files that don't need to be executed directly don't have a shebang line.
* `__init__.py` drops author's name and email address.
* `setup.py` gets version information from the `__init__.py`.

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/tsroten/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account and turn on the ReadTheDocs service hook.
* Release your package the standard Python way. Here's a release checklist: https://gist.github.com/audreyr/5990987

.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
