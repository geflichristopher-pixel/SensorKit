"""
Module: sensorkit/stats.py
Contributor: Christopher Gefli
Student ID: 94002029
Date: 05/08/2026
Role: Simple summary statistics for a list of numeric readings.

Complete the TODOs below.
"""

def mean(values):
    if not values:
        raise ValueError("The list cannot be empty")
    else:
        return sum(values) / len(values)

def minimum(values):
    if not values:
        raise ValueError("The list cannot be empty")
    return min(values)

def maximum(values):
    if not values:
        raise ValueError("The list cannot be empty")
    return max(values)

def spread(values):
    return max(values) - min(values)
    
        
        
                          
