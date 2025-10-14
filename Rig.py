"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Rig:
    def __init__(self, name, damage_counter, broken_state, storage, upgrade_level, damage_max):
        self.name = name
        self.damage_counter = 0
        self.broken_state = "Pristine"
        self.storage = ["Data Spike", "Data Spike", "Removable Drive"]
        self.upgrade_level = 0
        self.damage_max = 2

