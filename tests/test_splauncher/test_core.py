__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$May 18, 2015 22:08:21 EDT$"


import os
import shutil
import tempfile

from splauncher.core import main


class TestCore(object):
    def setup(self):
        self.tempdir = ""
        self.tempdir = tempfile.mkdtemp()

    def teardown(self):
        shutil.rmtree(self.tempdir)
        self.tempdir = ""

    def test_main_0(self):
        main("echo", "output")

        for each_filenames in os.listdir(self.tempdir):
            each_filenames = os.path.join(self.tempdir, each_filenames)

        assert ".err" in each_filenames[0]
        assert ".out" in each_filenames[1]

        with open(each_filenames[0], "r") as f:
            assert f.read() == ""

        with open(each_filenames[1], "r") as f:
            assert f.read() == "output"

    def test_main_1(self):
        main("echo", "error", "1>&2")

        for each_filenames in os.listdir(self.tempdir):
            each_filenames = os.path.join(self.tempdir, each_filenames)

        assert ".err" in each_filenames[0]
        assert ".out" in each_filenames[1]

        with open(each_filenames[0], "r") as f:
            assert f.read() == "error"

        with open(each_filenames[1], "r") as f:
            assert f.read() == ""
