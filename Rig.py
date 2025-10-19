"""
File: Rig.py
Description: Class for all Rig attributes and functions. Provides methods for initialising a rig, moving assets, repair and upgrade.
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from Asset import Asset
class Rig:
    """
    Class for all Rig attributes and functions.
    Provides methods for initialising a rig, moving assets, repair and upgrade.

    Attributes:
        - name (string): name of the Rig
        - damage counter (int): how much damage the Rig has
        - broken state (bool): if Rig is broken
        - upgrade level (int): level of upgrade
        - maximum damage (int): maximum damage level
        - storage (list): list of Rig assets

    """
    def __init__(self, name):
        """
        Initialises a Rig object.
        :param name:
                    - name (string): name of the Rig
                    - damage counter (int): how much damage the Rig has
                    - broken state (bool): if Rig is broken
                    - upgrade level (int): level of upgrade
                    - maximum damage (int): maximum damage level
                    - storage (list): list of Rig assets
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
        """
        Compiles a string of stored assets and returns current stats
        :return: (string, int, list)
        """
        # Join asset objects within rig storage for readability
        storage = ', '.join([str(asset) for asset in self.__storage])
        return (f"Rig: {self.__name}, Rig Condition: {self.rig_condition()}, Upgrade Level: {self.__upgrade_level}, Stored Assets: {storage}")

    def asset_gen(self):
        """
        Generates a random asset for this Rig.
        :return: print statement
        """
        assets = [
            Asset("CryptoToken", "Used to acquire or repair rigs."),
            Asset("Data Spike", "Used in battles."),
            Asset("Security Chip", "Used to encrypt or decrypt."),
            Asset("Hardware Patch", "Used to upgrade rigs."),
            Asset("Removable Drive", "Found in rigs and used for extraction.")
        ]
        # Generate random number within number of assets
        index = random.randrange(len(assets))
        new_asset = (assets[index])
        # Add new asset to rig storage
        self.__storage.append(new_asset)
        print(f"New Asset generated in {self.__name}'s storage: {new_asset}")

    def repair(self, hacker):
        """
        Repairs rig if damaged
        :param hacker: (Class) Class of hacker who is assigned rig
        :return: print statement
        """
        if hacker.scan("CryptoToken", 'inventory') is not None:
            # Check if rig damaged
            if self.__damage_counter > 0:
                # Reset damage and broken state
                self.__damage_counter = 0
                self.__broken_state = False
                print(f"{self.__name} has been repaired.")
            elif self.__damage_counter == 0:
                print("No repair needed.")

    def rig_condition(self):
        """
        Display rig condition
        :return: print statement
        """
        if self.__broken_state == False:
            return (f"Pristine (Level {self.__upgrade_level})")
        else:
            return (f"Broken (Level {self.__upgrade_level})")

    def upgrade_rig(self, hacker):
        """
        Upgrade rig
        :param hacker: (Class) Class of hacker who is assigned rig
        :return: (bool)
        """
        # Check for Hardware Patch in inventory
        if hacker.scan("Hardware Patch", 'inventory') is not None:
            # Check if upgrade level already at maximum (3)
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
        """
        Get rig storage
        :return: (list)
        """
        if isinstance(self.__storage, list):
            return self.__storage
        return []

    def get_broken_state(self):
        """
        Get Rig broken state
        :return: (bool)
        """
        return self.__broken_state

    def consume_asset(self, asset):
        """
        Consume asset from storage
        :param asset: (Class) Class of asset
        :return: print statement
        """
        if asset in self.__storage:
            self.__storage.remove(asset)
            print(f"{asset} used.")

    def store_asset(self, asset):
        """
        Store asset from inventory - add to storage
        :param asset: (Class) Class of asset
        :return: print statement
        """
        self.__storage.append(asset)
        print(f"{asset.name} stored in {self.__name}'s rig.")

    def retrieve_asset(self, asset):
        """
        Retrieve asset from storage - remove from storage
        :param asset: (Class) Class of asset
        :return: print statement
        """
        # Check if asset encrypted before moving
        if asset.get_encrypted() == False:
            self.__storage.remove(asset)
            print(f"{asset.name} retrieved from {self.__name}'s rig.")
        else:
            print(f"Cannot extract encrypted {asset.name}")

    def take_damage(self):
        """
        Take damage from Data Spike attack
        :return: print statement
        """
        self.__damage_counter += 1
        # Check if damage at max and adjust broken state
        if self.__damage_counter >= self.__damage_max:
            self.__broken_state = True
            print(f"{self.__name} is now broken.")
        else:
            print(f"{self.__name} damage increased to {self.__damage_counter}.")



