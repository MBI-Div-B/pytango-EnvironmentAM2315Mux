#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Copyright (C) 2020  MBI-Division-B
# MIT License, refer to LICENSE file
# Author: Luca Barbera / Email: barbera@mbi-berlin.de


from tango import AttrWriteType, DevState, DebugIt, ErrorIt, InfoIt, DeviceProxy
from tango.server import Device, attribute, command, device_property


class EnvironmentAM2315MuxSensor(Device):
    CtrlDevice = device_property(
        dtype="str",
        default_value="domain/family/memeber",
        )

    Channel = device_property(
        dtype="int",
        default_value=0,
        )

    temperature = attribute(label='Temperature',
                            access=AttrWriteType.READ,
                            dtype=float,
                            format='3.1f',
                            unit='C')

    humidity = attribute(label='Humidity',
                         access=AttrWriteType.READ,
                         dtype=float,
                         format='3.1f',
                         unit='%')

    def init_device(self):
        Device.init_device(self)
        self.set_state(DevState.INIT)
        try:
            self.ctrl = DeviceProxy(self.CtrlDevice)
            self.info_stream("Connection established.")
            self.set_state(DevState.ON)
        except Exception:
            self.error_stream('Connection could not be established.')
            self.set_state(DevState.OFF)

        self._temp = 0
        self._humid = 0

    def always_executed_hook(self):
        try:
            # _read_data measures both humidity and temperature
            self._temp, self._humid = self.ctrl.read_data(self.Channel)
        except Exception:
            self.error_stream('Data could not be read')

    def read_temperature(self):
        return self._temp

    def read_humidity(self):
        return self._humid


if __name__ == "__main__":
    EnvironmentAM2315MuxSensor.run_server()
