#!/usr/bin/python3 -u
from tango.server import run
import os
from EnvironmentAM2315MuxSensor import EnvironmentAM2315MuxSensor
from EnvironmentAM2315MuxCtrl import EnvironmEnvironmentAM2315MuxCtrlentAM2315Ctrl

# Run EnvironmentAM2315MuxCtrl and EnvironmentAM2315MuxSensor
run([EnvironmentAM2315MuxCtrl, EnvironmentAM2315MuxSensor])