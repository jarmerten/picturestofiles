import unittest
import os
import zipfile
import shutil
from picturestofiles import TEst


class MyTestCase(unittest.TestCase):


    def test_check_valid_path(self):
        filelocation = "C:\\Users\\Jared Merten\\Documents\\package.zip"
        TEst.check_valid_path(filelocation)
        self.assertEqual(filelocation, "C:\\Users\\Jared Merten\\Documents\\package.zip")

    def test_check_valid_path1(self):
        filelocation = "C:\\Users\\Jared Merten\\Documents\\packag"
        TEst.check_valid_path(filelocation)
        self.assertEqual(os.path.exists(filelocation), False)

if __name__ == '__main__':
    unittest.main()
