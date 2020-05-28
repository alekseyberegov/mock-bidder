import json
import unittest
from decimal import Decimal
from mockrtb.serialize.Array import Array
from mockrtb.serialize.String import String


class ArrayTestCase(unittest.TestCase):
    def setUp(self):
        self.array = None

    def tearDown(self):
        if self.array is not None:
            del self.array

    def test_string_array(self):
        self.array = Array(String)
        obj = self.array.deserialize(json.loads('["a","b","c"]'))
        self.assertListEqual(obj, ["a", "b", "c"])

    def test_decimal_array(self):
        self.array = Array(Decimal)
        obj = self.array.deserialize(json.loads('[1.1, 2.2, 3.3]'))
        self.assertListEqual(obj, [1.1, 2.2, 3.3])


