import unittest2

from modbusreader import structutils

__author__ = "Stephan Müller"
__copyright__ = "2018, Stephan Müller"
__license__ = "MIT"


class StructUtilsTests(unittest2.TestCase):

    def test_get_format(self):
        with self.assertRaises(ValueError):
            structutils.get_format("nonexisting_data_type")

    def test_calcsize(self):
        self.assertEqual(structutils.calcsize("int16"), 2)
        self.assertEqual(structutils.calcsize("int32"), 2)
        self.assertEqual(structutils.calcsize("uint32"), 4)
        self.assertEqual(structutils.calcsize("float"), 4)
        self.assertEqual(structutils.calcsize("byte"), 1)

    def test_int16list_to_bytes(self):
        int16_list = [0, 1]
        self.assertEqual(structutils.int16list_to_bytes(int16_list),  b'\x00\x00\x00\x01')

    def test_bytes_to_datatype(self):
        byte_list = b'\x00\x00'
        data_type = "int16"
        self.assertEqual(structutils.bytes_to_datatype(byte_list, data_type), 0)

        byte_list = b'\x00\x01'
        data_type = "int16"
        self.assertEqual(structutils.bytes_to_datatype(byte_list, data_type), 1)


if __name__ == '__main__':
    unittest2.main()
