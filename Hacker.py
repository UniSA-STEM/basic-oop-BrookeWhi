"""
File: Hacker.py
Description: All hacker function and attributes
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig

class Hacker:
    """
    Class for Hacker attributes and function
    Contains methods for initialising hacker and acquiring and utilising rig and asset functionality
    Attributes:
        - name (str): name of the Hacker
        - inventory (list): assets stored in inventory
        - rig (Class): Rig class
        - trace level (int): trace level
    """
    def __init__(self, name):
        """
        Initialises Hacker
        :param name:
            - name (str): name of the Hacker
            - inventory (list): assets stored in inventory
            - rig (Class): Rig class
            - trace level (int): trace level
        """
        self.__name = name
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = ""
        self.__trace_level = 0

    def __str__(self):
        """
        Compiles a string of stored assets and returns current stats
        :return: (string, int, list)
        """
        # Join inventory objects
        inventory = ', '.join([str(asset) for asset in self.__inventory])
        return (f"Hacker: {self.__name}, Rig: {self.__rig.name}, Trace Level: {self.__trace_level}, Inventory: {inventory}")

    def get_inventory(self):
        """
        Returns current inventory
        :return: (list)
        """
        return self.__inventory

    def get_rig(self):
        """
        Returns current rig
        :return: (Class) Rig
        """
        if isinstance(self.__rig, str):
            print("Hacker has no rig.")
            return None
        return self.__rig

    def get_inventory_item(self, item):
        """
        Get an item from the inventory.
        :param item: (String) The name of the item.
        :return: (Class, String) or print statement
        """
        # Iterate through inventory until item found
        for i in self.__inventory:
            if i.get_name() == item:
                return i, "inv"
        # Iterate through rig storage until item found
        for i in self.__rig.get_storage():
            if i.get_name() == item:
                return i, "rig"
        # If item not found return print statement
        return print('No item found.')

    def consume_asset(self, asset):
        """
        Consume asset from inventory.
        :param asset: (String) Name of asset to consume.
        :return: print statement
        """
        item, loc = self.scan(asset, 'inventory')
        if item is not None:
            self.__inventory.remove(item)
            print(f"{asset} consumed from inventory.")
        else:
            print(f"{asset} not found in inventory.")


    def acquire_rig(self):
        """
        Acquire rig
        :return: print statement
        """
        scan = self.scan("CryptoToken", 'inventory')
        if scan == (None, None):
            print("No token available to acquire rig")
            return
        else:
            if self.__rig == "":
                self.consume_asset("CryptoToken")
                self.__rig = Rig(self.__name)
                print(f"{self.__name} has acquired {self.__rig.name}")
            else:
                print("Hacker already has a rig.")


    def use_asset(self, asset, target=None):
        """
        Use asset from inventory.
        :param asset: (String) Name of asset to use.
        :param target: (String) Name of asset to use. or (string) name of target hacker
        :return: (bool/None)
        """
        if isinstance(asset, str):
            string = asset
            asset, loc = self.scan(string)

        if not asset or not loc:
            print(f"{string} not found in inventory.")
            return

        # CryptoToken use
        if asset.name == "CryptoToken":
            scan = self.scan("CryptoToken", 'inventory')
            if scan == (None, None):
                print("Need CryptoToken.")
            else:
                self.__rig.repair(self)
                self.consume_asset("CryptoToken")

        # Data Spike use
        elif asset.name == "Data Spike":
            scan = self.scan("Data Spike", 'inventory')
            if scan == (None, None):
                print("Need Data Spike.")
            else:
                # Check trace level is not max
                if self.__trace_level < 5:
                    self.consume_asset("Data Spike")
                    # Apply damage to target rig
                    target.__rig.take_damage()
                    self.increase_trace_level()
                else:
                    print("Trace level is too high.")

        # Hardware Patch use
        elif asset.name == "Hardware Patch":
            if self.__rig == "":
                print("No Rig to upgrade.")
                return False
            if self.scan("Hardware Patch", 'inventory') is not None:
                self.consume_asset("Hardware Patch")
                self.__rig.upgrade_rig(self)
            else:
                print("Need Hardware Patch.")

        # Removable Drive use
        elif asset.name == "Removable Drive":
            scan = self.scan("Removable Drive", 'inventory')
            if scan == (None, None):
                print("Need Removable Drive.")
            else:
                if target is not None:
                    target_rig = target.__rig
                    if target_rig is not None:
                        # Check target rig condition
                        if target_rig.get_broken_state() == True:
                            self.consume_asset("Removable Drive")
                            # Retrieve all assets from target rig
                            target_rig.retrieve_asset(asset, True)

                            self.increase_trace_level()
                        else:
                            print("Target not broken.")
                    else:
                        print("Target has no rig.")
                else:
                    print("No target specified for extraction.")


        # Security Chip use
        elif asset.name == "Security Chip":
            # Ensure asset specified for encrypt/decrypt
            if target is None:
                print("No target asset specified for encryption/decryption.")
                return None
            # Find asset in inventory
            target_asset, target_loc = self.scan(target)
            if target_asset is None:
                print(f"{target} not found in inventory.")
            scan = self.scan("Security Chip", 'inventory')
            if scan == (None, None):
                print("Need Security Chip.")
            else:
                self.consume_asset("Security Chip")
                # Encrypt or Decrypt based on current status
                if target_asset.get_encrypted() == False:
                    target_asset.encrypt()
                elif target_asset.get_encrypted() == True:
                    target_asset.decrypt()


    def extract_assets(self, target):
        """
        Extract assets from target storage.
        :param target: (class) Target rig
        :return: print statement
        """
        if self.scan("Removable Drive", 'inventory') is not None:
            target_rig = target.__rig
            # Ensure rig broken before extracting assets
            if target_rig.get_broken_state() == True:
                for asset in target_rig.get_storage():
                    if asset.__encrypted == False:
                        self.__inventory.append(asset)
                        target_rig.get_storage().remove(asset)
            else:
                print("Target rig is not broken, cannot extract assets.")
        else:
            print("Target has no rig.")

    def store_asset(self, name):
        """
        Store asset from inventory.
        :param name: (string) Name of asset
        :return: print statement
        """
        asset, loc = self.scan(name, 'inventory')
        if asset is None:
            print(f"{asset.name} not found in inventory.")
        else:
            # Check if encrypted, only store unencrypted
            if asset.get_encrypted() == False:
                stored = self.__rig.store_asset(asset)
                if stored:
                    self.__inventory.remove(asset)
                    self.increase_trace_level()

            elif asset.get_encrypted() == True:
                print(f"{asset.name} is encrypted and cannot be stored.")


    def retrieve_asset(self, name):
        """
        Retrieve asset from storage
        :param name: (string) Name of asset
        :return: print statement
        """
        asset, loc = self.scan(name, 'rig')
        if asset is None:
            print(f"{asset} not found in rig storage.")
        else:
            # Check encryption status
            if not asset.get_encrypted():
                # Check trace level below max
                if self.__trace_level < 5:
                    self.__rig.retrieve_asset(asset)
                    self.__inventory.append(asset)
                    self.increase_trace_level()
                else:
                    print("Trace level is too high.")
            elif asset.get_encrypted() == True:
                print(f"{asset} is encrypted and cannot be retrieved.")



    def scan(self, name, loc = 'both'):
        """
        Search for assets in inventory and rig storage.
        :param name: (string) Name of asset
        :param loc: (string) Location of asset
        :return: (Class) asset or None
        """
        if loc in ('both', 'inventory'):
            for i in self.__inventory:
                if i.name == name:
                    return i, 'inventory'
        if loc in ('both', 'rig'):
            for i in self.__rig.get_storage():
                if i.name == name:
                    return i, 'rig'
        return None, None

    def add_asset(self, asset, loc='inventory'):
        """
        Add asset to inventory. (For testing purposes)
        :param asset: (string) Name of asset
        :param loc: (string) Location of asset
        :return: print statement
        """
        new_asset = Asset(asset, None)
        if loc == 'inventory':
            self.__inventory.append(new_asset)
        elif loc == 'rig':
            self.__rig.store_asset(new_asset)
        print(f"{asset} added to {loc}.")

    def remove_asset(self, asset, loc='inventory'):
        """
        Remove asset from inventory. (For testing purposes)
        :param asset: (string) Name of asset
        :param loc: (string) Location of asset
        :return: print statement
        """
        if isinstance(asset, str):
            string = asset
            asset, loc = self.scan(string)

        if asset is None:
            print(f"{string} not found in inventory.")
            return

        if loc == 'inventory':
            self.__inventory.remove(asset)
        elif loc == 'rig':
            self.__rig.retrieve_asset(asset)
            self.__inventory.remove(asset)

        print(f"{asset.name} has been removed from {loc}.")

    def increase_trace_level(self):
        """
        Increase trace level.
        :return: print statement
        """
        if self.__trace_level > 4:
            print(f"Trace level maxxed out, wait to cool down.")
        else:
            self.__trace_level += 1
            print(f"Trace level increased to {self.__trace_level}.")

    def reduce_trace_level(self):
        """
        Reduce trace level.
        :return: print statement
        """
        if self.__trace_level == 0:
            return
        self.__trace_level -= 1
        print(f"Trace level reduced to {self.__trace_level}.")

    def asset_gen(self):
        """
        Asset generator
        :return: print statement
        """
        self.__rig.asset_gen()
        return
