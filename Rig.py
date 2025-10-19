"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset
class Rig:
    """

    """
    def __init__(self, name):
        """

        :param name:
        """
        self.name = name
        self.__name = name
        self.__damage_counter = 0
        self.__broken_state = False
        self.__upgrade_level = 0
        self.__damage_max = 2
        self.__storage = [Asset("Data Spike", "Used in battles."),
                          Asset("Data Spike", "Used in battles."),
                          Asset("Removable Drive", "Found in rigs and used for extraction.")]

    def __str__(self):
        storage = ', '.join([str(asset) for asset in self.__storage])
        return (f"Rig: {self.__name}, Rig Condition: {self.rig_condition()}, Upgrade Level: {self.__upgrade_level}, Stored Assets: {storage}")

    def asset_gen(self):
        assets = [
            Asset("CryptoToken", "Used to acquire or repair rigs."),
            Asset("Data Spike", "Used in battles."),
            Asset("Security Chip", "Used to encrypt or decrypt."),
            Asset("Hardware Patch", "Used to upgrade rigs."),
            Asset("Removable Drive", "Found in rigs and used for extraction.")
        ]
        index = random.randrange(len(assets))
        new_asset = (assets[index])
        self.__storage.append(new_asset)
        print(f"New Asset generated in {self.__name}'s storage: {new_asset}")

    def repair(self, hacker):
        if hacker.scan("CryptoToken", 'inventory') is not None:
            if self.__damage_counter > 0:
                self.__damage_counter = 0
                self.__broken_state = False
                print(f"{self.__name} has been repaired.")
            elif self.__damage_counter == 0:
                print("No repair needed.")

    def rig_condition(self):
        if self.__broken_state == False:
            return (f"Pristine (Level {self.__upgrade_level})")
        else:
            return (f"Broken (Level {self.__upgrade_level})")

    def upgrade_rig(self, hacker):
        if hacker.scan("Hardware Patch", 'inventory') is not None:
            if self.__upgrade_level < 3:
                self.__upgrade_level += 1
                self.__damage_max += 1
                print(f"{self.__name}'s rig has been upgraded to level {self.__upgrade_level}.")
                return True
            else:
                print(f"{self.__name}'s rig already at Max level.")
        else:
            print("Need Hardware Patch.")
            return False

    def get_storage(self):
        if isinstance(self.__storage, list):
            return self.__storage
        return []

    def get_broken_state(self):
        return self.__broken_state

    def use_storage_item(self, item):
        for i in self.__storage:
            if i.get_name() == item:
                print(i)
                self.consume_asset(item)
        return print('No such asset found.')

    def consume_asset(self, asset):
        if asset in self.__storage:
            self.__storage.remove(asset)
            print(f"{asset} used.")

    def store_asset(self, asset):
        self.__storage.append(asset)
        print(f"{asset.name} stored in {self.__name}'s rig.")

    def retrieve_asset(self, asset):
        if asset.get_encrypted() == False:
            self.__storage.remove(asset)
            print(f"{asset.name} retrieved from {self.__name}'s rig.")
        else:
            print(f"Cannot extract encrypted {asset.name}")

    def take_damage(self):
        self.__damage_counter += 1
        if self.__damage_counter >= self.__damage_max:
            self.__broken_state = True
            print(f"{self.__name} is now broken.")
        else:
            print(f"{self.__name} damage increased to {self.__damage_counter}.")



