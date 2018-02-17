import unittest2
import json
import os

from modbusreader import ModbusReader

__author__ = "Stephan Müller"
__copyright__ = "2017, Stephan Müller"
__license__ = "MIT"

__dirname__ = os.path.dirname(os.path.abspath(__file__))

class ModbusReaderTests(unittest2.TestCase):

    CONFIG = "config.json"

    @classmethod
    def setUpClass(cls):
        #cls.modbusreader = ModbusReader("localhost", 502, 0, "config.json")
        pass

    def test_goup_modbus_device_definition(self):
        ModbusReader.group_modbus_device_definition(
            json.loads(open(__dirname__ + "/" + self.CONFIG, 'rb').read().decode("UTF-8"))
        )
