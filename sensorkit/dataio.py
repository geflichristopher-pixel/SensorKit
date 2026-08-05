"""
Module: sensorkit/dataio.py
Contributor: <Kwame Ewusi Boateng>
Student ID: <10182029>
Date: <5th August 2029>
Role: Load raw sensor readings from a text/CSV file, safely.

Uses pathlib for the file path and exceptions to handle problems.
Complete the TODOs below.
"""
from pathlib import Path


def load_readings(filepath):
    """
    #     Read a file of raw numeric readings, one value per line, and return
    #     a list of floats.
    #
    #     Rules:
    #       - If the file does not exist, raise FileNotFoundError.
    #       - Ignore blank lines.
    #       - If a line is not a valid number, skip it and print a short message
    #         instead of letting the program crash.
    #     """
    path = Path(filepath)

    # TODO : if the path does not exist, raise FileNotFoundError
    if not path.is_file():
        raise FileNotFoundError(f'File not found: {filepath}')

    readings = []
    # TODO : Complete the loop to read in the file content
    #         TODO : try to convert `line` to a float and append it to readings.
    #                 If it raises ValueError, print:
    #                 f"Skipping invalid line: {line!r}"

    with path.open('r') as file:
        for line in file:
            line_str = line.strip()

            if not line_str:
                continue

            try:
                value = float(line_str)
                readings.append(value)

            except ValueError:
                print(f"Skipping invalid line: {line_str!r}")

    return readings


