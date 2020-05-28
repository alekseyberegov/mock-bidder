import unittest
from decimal import Decimal
from mockrtb.serialize.Field import Field


class FieldTestCase(unittest.TestCase):
    def setUp(self):
        self.field = None

    def tearDown(self):
        if self.field is not None:
            del self.field

    def test_decimal_field(self):
        self.field = Field(Decimal)
        self.assertEqual(type(self.field.deserialize("1.23")), Decimal)

    def test_string_field(self):
        self.field = Field(str)
        self.assertEqual(type(self.field.deserialize("1.23")), str)
