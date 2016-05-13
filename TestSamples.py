import unittest
import os
import zipfile
import shutil
from picturestofiles import TEst


class MyTestCase(unittest.TestCase):


    def test_main(self):
        filelocation = "C:\\Users\\Jared Merten\\Documents\\package.zip"
        TEst.check_valid_path(filelocation)
        self.assertEqual(filelocation, "C:\\Users\\Jared Merten\\Documents\\package.zip")


if __name__ == '__main__':
    unittest.main()
