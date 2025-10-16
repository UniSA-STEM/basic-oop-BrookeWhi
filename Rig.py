"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random

class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__storage = [Asset("Data Spike", "Used in battles."), Asset("Data Spike", "Used in battles."), Asset("Removable Drive", "Found in rigs and used for extraction.")]
        self.__upgrade_level = 0
        self.__damage_max = 2

    def asset_gen(self):
        assets = [
            ("CryptoToken", "Used to acquire or repair rigs."),
            ("Data Spike", "Used in battles."),
            ("Security Chip", "Used to encrypt or decrypt."),
            ("Hardware Patch", "Used to upgrade rigs."),
            ("Removable Drive", "Found in rigs and used for extraction.")
        ]
        index = random.randrange(len(assets))
        new_asset = (assets[index])
        self.__storage.append(new_asset)

    def repair(self, Hacker):
        if "CryptoToken" in Hacker.get_inventory():
            if self.__damage_counter > 0:
                self.__damage_counter = 0
                self.__broken_state = False
                Hacker.consume_asset("CryptoToken")
            else:
                print("No repair needed")
        else:
            print("CryptoToken needed for repair")

    def rig_condition(self):
        if self.__broken_state == False:
            return (f"Pristine (Level {self.__upgrade_level})")
        else:
            return (f"Broken (Level {self.__upgrade_level})")

    def upgrade_rig(self, hacker):
        if "Hardware Patch" in hacker.get_inventory():
            hacker.consume_asset("Hardware Patch")
            self.__upgrade_level = self.__upgrade_level + 1
            self.__damage_max = self.__damage_max + 1
        else:
            print("No Hardware Patch")

    def __str__(self):
        return (f"Rig: {self.__name}, Rig Condition: {self.rig_condition()}, Upgrade Level: {self.__upgrade_level}, Stored Assets: {self.__storage}")

    def get_storage(self):
        return self.__storage

