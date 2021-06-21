#!/usr/bin/python3 -u
from tango.server import run
import os
from EnvironmentAM2315Sensor import EnvironmentAM2315Sensor
from EnvironmentAM2315Ctrl import EnvironmentAM2315Ctrl

# Run EnvironmentAM2315Ctrl and EnvironmentAM2315Sensor
run([EnvironmentAM2315Ctrl, EnvironmentAM2315Sensor])