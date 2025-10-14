"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Rig import Rig
from Asset import Asset

class Hacker:
    def __init__(self, name):
        self.name = name
        self.inventory = ["CryptoToken"]
        self.rig = ""
        self.trace_level = 0

