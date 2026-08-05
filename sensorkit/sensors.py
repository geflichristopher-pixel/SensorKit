"""
Module: sensorkit/sensors.py
Contributor: Lynn Mudzengerere
Student ID: 07682029
Date: 05/08/2026
Role: Provide concrete sensor classes built on the Sensor base class.

Each class must implement both abstract methods: read() and units().
Complete the TODOs below.
"""
from .base import Sensor


class Thermocouple(Sensor):
    def read(self, raw):
        # TODO: `raw` is in millivolts. Return degrees Celsius using:
        #       raw * 24.9 - 0.4
        return raw* 24.9 - 0.4
    def units(self):
        return "C"
        #pass

    #TODO Implement missing method that returns the string "C"


class PressureGauge(Sensor):
    def read(self, raw):
        # TODO: `raw` is in volts. Return bar using:
        #       raw * 2.5
        return raw*2.5
        #pass

    def units(self):
        # TODO: return the string "bar"
        return "bar"
        #pass

class StrainGauge(Sensor):
    """Concrete sensor for measuring mechanical strain."""

    def read(self, raw):
        """Calibrate raw signal to strain in microstrain."""
        return raw * 1000.0

    def units(self):
        """Return unit of measurement."""
        return "microstrain"


# TODO (optional, only if you have time):
# Add a third class StrainGauge where read(raw) returns raw * 1000
# and units() returns "microstrain".
