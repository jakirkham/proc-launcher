|PyPI| |conda-forge| |Documentation| |Travis| |Wercker| |Coverage| |Health| |License|

--------------

splauncher
==========


Motivation
----------

This provides a simple tool for launching jobs using DRMAA. In particular, it
launches the given command so that it starts in the current working directory,
with the same environment variables, determines a job name derived from the
command line call and time of launch, and finally automatically reroutes
``stdout`` and ``stderr`` to files named after the job.


Prerequisites
-------------

Installation and testing requires |setuptools|_. Documentation relies on
|sphinx|_. Running relies upon proper installation and configuration of
|drmaa-python|_.

.. |drmaa-python| replace:: ``drmaa-python``
.. _drmaa-python: https://github.com/pygridtools/drmaa-python
.. |setuptools| replace:: ``setuptools``
.. _setuptools: http://pythonhosted.org/setuptools/
.. |sphinx| replace:: ``sphinx``
.. _sphinx: http://sphinx-doc.org/


Installation
------------

Assuming the proper prerequisites, installation can be done the standard python
way (as seen below).

.. code-block:: sh

    python setup.py install


.. |PyPI| image:: https://img.shields.io/pypi/v/splauncher.svg
   :target: https://pypi.python.org/pypi/splauncher
.. |Travis| image:: https://travis-ci.org/jakirkham/splauncher.svg?branch=master
   :target: https://travis-ci.org/jakirkham/splauncher
.. |Wercker| image:: https://app.wercker.com/status/247fda859ed4812b68491a4fa5839876/s/master
   :target: https://app.wercker.com/project/bykey/247fda859ed4812b68491a4fa5839876
.. |Coverage| image:: https://coveralls.io/repos/jakirkham/splauncher/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/jakirkham/splauncher?branch=master
.. |Health| image:: https://landscape.io/github/jakirkham/splauncher/master/landscape.svg?style=flat
   :target: https://landscape.io/github/jakirkham/splauncher/master
.. |License| image:: https://img.shields.io/github/license/jakirkham/splauncher.svg
   :target: ./LICENSE.txt
.. |Documentation| image:: https://readthedocs.org/projects/splauncher/badge/?version=latest
   :target: https://splauncher.readthedocs.io/en/latest/?badge=latest
.. |conda-forge| image:: https://anaconda.org/conda-forge/splauncher/badges/version.svg
   :target: https://anaconda.org/conda-forge/splauncher
