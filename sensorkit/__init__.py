"""
sensorkit package
A small in-class sensor data toolkit assembled by the whole team.

This file is the ASSEMBLY step (done together once every module is complete).
It exposes the public API so a user can simply write:

    from sensorkit import Thermocouple, load_readings, summarise

If you add a StrainGauge class in sensors.py, add it to the import below too.
"""
#example from .base import Sensor


from .base import Sensor
from .sensors import Thermocouple, PressureGauge
from .report import summarise
from .dataio import load_readings
from .stats import mean, minimum, maximum, spread

__all__ = [
    "Sensor",
    "Thermocouple",
    "PressureGauge",
    "StrainGauge",
    "load_readings",
    "mean",
    "minimum",
    "maximum",
    "spread",
    "summarise",
]
