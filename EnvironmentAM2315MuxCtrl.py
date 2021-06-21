#!/usr/bin/python3 -u
# coding: utf8
# PhytronMCC2Ctrl
from tango import DevState, AttrWriteType, DispLevel
from tango.server import Device, attribute, command, device_property
import AM2315
from Adafruit_GPIO import I2C


class EnvironmentAM2315MuxCtrl(Device):
    # device properties
    Address = device_property(
        dtype="str",
        default_value="0x70",
    )

    def init_device(self):
        Device.init_device(self)
        self.set_state(DevState.INIT)
        try:
            self.mux = I2C.get_i2c_device(address=int(self.Address, 16))
            self.sensor = AM2315.AM2315()
            self.set_state(DevState.ON)
        except:
            self.set_state(DevState.OFF)
            self.error_stream('Cannot connect!')

    @command(dtype_in=int, dtype_out=(float,))
    def read_data(self, channel):
        try:
            self.mux_select(channel)
            self.sensor._read_data()
            return self.sensor.temperature, self.sensor.humidity
        except:
            return -1, -1

    def mux_select(self, channel):
        if channel > 7:
            return
        self.mux.writeRaw8(1 << channel)

if __name__ == "__main__":
    EnvironmentAM2315MuxCtrl.run_server()
