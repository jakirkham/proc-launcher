from __future__ import print_function


__author__ = "John Kirkham <kirkhamj@janelia.hhmi.org>"
__date__ = "$May 18, 2015 22:08:21 EDT$"


import os
import shutil
import tempfile
import time

from splauncher.core import main


class TestCore(object):
    def setup(self):
        self.cwd = os.getcwd()
        self.tempdir = ""
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

        print("tempdir = \"%s\"" % self.tempdir)

    def teardown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.tempdir)
        self.tempdir = ""
        self.cwd = ""

    def test_main_0(self):
        main("",
            "python",
            "-c",
            "from __future__ import print_function;" +
            "import sys;" +
            "print(\"output\", file=sys.stdout)"
        )
        time.sleep(5)

        filenames = []
        for each_filename in os.listdir(self.tempdir):
            filenames.append(os.path.join(self.tempdir, each_filename))

        assert ".err" in filenames[0]
        assert ".out" in filenames[1]

        with open(filenames[0], "r") as f:
            s = f.read().strip()
            print("File \"%s\" contains \"%s\"." % (f.name, s))
            assert s == ""

        with open(filenames[1], "r") as f:
            s = f.read().strip()
            print("File \"%s\" contains \"%s\"." % (f.name, s))
            assert s == "output"

    def test_main_1(self):
        main("",
            "python",
            "-c",
            "from __future__ import print_function;" +
            "import sys;" +
            "print(\"error\", file=sys.stderr)"
        )
        time.sleep(5)

        filenames = []
        for each_filename in os.listdir(self.tempdir):
            filenames.append(os.path.join(self.tempdir, each_filename))

        assert ".err" in filenames[0]
        assert ".out" in filenames[1]

        with open(filenames[0], "r") as f:
            s = f.read().strip()
            print("File \"%s\" contains \"%s\"." % (f.name, s))
            assert s == "error"

        with open(filenames[1], "r") as f:
            s = f.read().strip()
            print("File \"%s\" contains \"%s\"." % (f.name, s))
            assert s == ""
