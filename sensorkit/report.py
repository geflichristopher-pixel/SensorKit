"""
Module: sensorkit/report.py
Contributor: Ahalam Maliboto Azangina
Student ID: 04532029
Date: 5th August, 2026
Role: Produce a printed summary of calibrated readings for one sensor.

This module ties together a sensor (from sensors.py) and the statistics
functions (from stats.py). Complete the TODOs below.
"""
from .stats import mean, minimum, maximum, spread


def summarise(sensor, raw_readings):
    """
    Given a sensor object and a list of raw readings:
      1. Calibrate every raw reading using sensor.read(...)
      2. Print a short summary using the stats functions.
    
    """
    count = len(raw_readings)
    calibrated = []
    for r in raw_readings:
      calibrated.append(sensor.read(r))
      
    u = sensor.units()
    
    report =""
    report+= f"Report for {sensor.name} \n "
    report+= f"count: {count} \n"
    report+= f"mean: {mean(calibrated):.2f} {u} \n"
    report+= f"min: {minimum(calibrated):.2f} {u}\n"
    report+= f"max: {maximum(calibrated):.2f} {u} \n"
    report+= f"spread: {spread(calibrated):.2f} {u} \n"
    
    return report
    
    
    # TODO : build a list `calibrated` containing sensor.read(r)
    #         for every r in raw_readings
    # TODO : get the unit string from sensor.units() and store it in `u`
    # TODO : print the report. Suggested lines (format numbers to 2 d.p.):
    #         Report for <sensor.name>
    #           count:   <how many readings>
    #           mean:    <mean> <u>
    #           min:     <minimum> <u>
    #           max:     <maximum> <u>
    #           spread:  <spread> <u>
    
