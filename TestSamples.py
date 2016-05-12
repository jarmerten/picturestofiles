import unittest
import os
import zipfile
import shutil
from picturestofiles import TEst


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertTrue(True)

    def test_main(self):


    def test_valid_path(self):
        filelocation = "C:\\Users\\Jared Merten\\Documents\\package.zip"
        TEst.check_valid_path(filelocation)
        self.assertTrue(os.path.exists(filelocation), True)
        TEst.replace_original()


    def test_valid_path(self):
        filelocation = "C:\\Users\\Jared Merten\\Documents\\package.zip"
        TEst.check_valid_path(filelocation)
        self.assertEqual(filelocation, "C:\\Users\\Jared Merten\\Documents\\package.zip")
        TEst.replace_original()



if __name__ == '__main__':
    unittest.main()
