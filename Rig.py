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
        self.__damage_counter = 10
        self.__broken_state = True
        self.__storage = [("Data Spike", "Used in battles."), ("Data Spike", "Used in battles."), ("Removable Drive", "Found in rigs and used for extraction.")]
        self.__upgrade_level = 0
        self.__damage_max = 2

    def assetGen(self):
        assets = ["CryptoToken", "Data Spike", "Removable Drive", "Security Chip", "Hardware Patch"]
        asset_desc = ["Used to acquire or repair rigs.", "Used in battles.", "Found in rigs and used for extraction.",
                      "Used to encrypt or decrypt.", "Used to upgrade rigs."]
        index = random.randrange(len(assets))
        new_asset = [(assets[index], asset_desc[index])]
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

    def __str__(self):
        return (f"Rig: {self.__name}, Rig Condition: {self.rig_condition()}, Upgrade Level: {self.__upgrade_level}, Stored Assets: {self.__storage}")


