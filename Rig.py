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
        self.__broken_state = "Pristine"
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

### Testing
# x = Rig("PC")
# print(x._Rig__storage)
# x.assetGen()
# print(x._Rig__storage)