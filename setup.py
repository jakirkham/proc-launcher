__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$May 18, 2015 12:09:31 EDT$"


from glob import glob

from setuptools import setup, find_packages


build_requires = []
install_requires = []
tests_require = ["nose"]

setup(
    name="subprocess-launcher",
    version="",
    description="A simple subprocess launcher with optional DRMAA support.",
    url="https://github.com/jakirkham/subprocess-launcher",
    license="BSD",
    author="John Kirkham",
    author_email="kirkhamj@janelia.hhmi.org",
    scripts=glob("bin/*"),
    packages=find_packages(exclude=["tests*"]),
    build_requires=build_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="nose.collector",
    zip_safe=True
)
