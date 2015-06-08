|Build Status| |Coverage Status| |Code Health| |License| |Documentation| |Binstar Release|

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

Installation requires |setuptools|_. Testing relies on |nose|_. Documentation
relies on |sphinx|_. Running relies upon proper installation and configuration
of |drmaa-python|_.

.. |drmaa-python| replace:: ``drmaa-python``
.. _drmaa-python: https://github.com/pygridtools/drmaa-python
.. |nose| replace:: ``nose``
.. _nose: http://nose.readthedocs.org/en/latest/
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


.. |Build Status| image:: https://travis-ci.org/jakirkham/splauncher.svg?branch=master
   :target: https://travis-ci.org/jakirkham/splauncher
.. |Coverage Status| image:: https://coveralls.io/repos/jakirkham/splauncher/badge.svg?branch=master
   :target: https://coveralls.io/r/jakirkham/splauncher?branch=master
.. |Code Health| image:: https://landscape.io/github/jakirkham/splauncher/master/landscape.svg?style=flat
   :target: https://landscape.io/github/jakirkham/splauncher/master
.. |License| image:: http://img.shields.io/badge/license-BSD-3-Clause-blue.svg
   :target: http://opensource.org/licenses/BSD-3-Clause
.. |Documentation| image:: https://img.shields.io/badge/license-BSD%203--Clause-blue.svg
   :target: http://jakirkham.github.io/splauncher/
.. |Binstar Release| image:: https://binstar.org/jakirkham/splauncher/badges/version.svg
   :target: https://binstar.org/jakirkham/splauncher
