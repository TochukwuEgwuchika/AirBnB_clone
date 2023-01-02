import sys, os, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

from models.base_model import BaseModel
import unittest
from models.base_model import BaseModel

#Module for testing the base model

class TestBaseModel(unittest.TestCase):
    #class for testings base model
    def test_save
