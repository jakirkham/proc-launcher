subprocess-launcher
===================


Motivation
----------

This provides a simple tool for launching jobs using DRMAA. In particular, it
launches the given command so that it starts in the current working directory,
with the same environment variables, determines a job name derived from the
command line call and time of launch, and finally automatically reroutes
``stdout`` and ``stderr`` to files named after job.
