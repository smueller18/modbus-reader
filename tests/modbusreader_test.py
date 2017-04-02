import os
from modbusreader import ModbusReader


modbus = ModbusReader("localhost", 502, 1, "test")
