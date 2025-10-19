"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
from Rig import Rig

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken")]
        self.__rig = ""
        self.__trace_level = 0

    def __str__(self):
        inventory = ', '.join([str(asset) for asset in self.__inventory])
        return (f"Hacker: {self.__name}, Rig: {self.__rig.name}, Trace Level: {self.__trace_level}, Inventory: {inventory}")

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        if isinstance(self.__rig, str):
            print("Hacker has no rig.")
            return None
        return self.__rig

    def get_inventory_item(self, item):
        """
        Get an item from the inventory.
        :param item: (String) The name of the item.
        :return: (Class, String) or Print Statement
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
        """
        item, loc = self.scan(asset, 'inventory')
        if item is not None:
            self.__inventory.remove(item)
            print(f"{asset} consumed from inventory.")
        else:
            print(f"{asset} not found in inventory.")


    def acquire_rig(self):
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
        if isinstance(asset, str):
            string = asset
            asset, loc = self.scan(string)

        if not asset or not loc:
            print(f"{string} not found in inventory.")
            return

        # CryptoToken
        if asset.name == "CryptoToken":
            if self.scan("CryptoToken", 'inventory') is not None:
                self.__rig.repair(self)
                self.consume_asset("CryptoToken")
            else:
                print("Need CryptoToken.")
        # Data Spike
        elif asset.name == "Data Spike":
            if self.scan("Data Spike", 'rig') is not None:
                if self.__trace_level < 5:
                    self.consume_asset("Data Spike")
                    target.__rig.take_damage()
                    self.increase_trace_level()
                else:
                    print("Trace level is too high.")
            else:
                print("Need Data Spike.")
        # Hardware Patch
        elif asset.name == "Hardware Patch":
            if self.__rig == "":
                print("No Rig to upgrade.")
                return False
            if self.scan("Hardware Patch", 'inventory') is not None:
                self.consume_asset("Hardware Patch")
                self.__rig.upgrade_rig(self)
            else:
                print("Need Hardware Patch.")

        # Removable Drive
        elif asset.name == "Removable Drive":
            scan = self.scan("Removable Drive", 'inventory')
            if scan == (None, None):
                print("Need Removable Drive.")
            else:
                if target is not None:
                    target_rig = target.__rig
                    if target_rig is not None:
                        if target_rig.get_broken_state() == True:
                            self.consume_asset("Removable Drive")
                            for item in target_rig.get_storage():
                                target_rig.retrieve_asset(item)

                            self.increase_trace_level()
                        else:
                            print("Target not broken.")
                    else:
                        print("Target has no rig.")
                else:
                    print("No target specified for extraction.")


        # Security Chip
        elif asset.name == "Security Chip":
            if target is None:
                print("No target asset specified for encryption/decryption.")
                return

            target_asset, target_loc = self.scan(target)

            if target_asset is None:
                print(f"{target} not found in inventory.")

            scan = self.scan("Security Chip", 'inventory')
            if scan == (None, None):
                print("Need Security Chip.")
            else:
                self.consume_asset("Security Chip")
                if target_asset.get_encrypted() == False:
                    target_asset.encrypt()
                elif target_asset.get_encrypted() == True:
                    target_asset.decrypt()


    def extract_assets(self, target):
        if self.scan("Removable Drive", 'inventory') is not None:
            target_rig = target.__rig
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
        asset, loc = self.scan(name, 'inventory')
        if asset is None:
            print(f"{asset.name} not found in inventory.")
        else:
            if asset.get_encrypted() == False:
                self.__rig.store_asset(asset)
                self.__inventory.remove(asset)
                self.increase_trace_level()

            elif asset.get_encrypted() == True:
                print(f"{asset.name} is encrypted and cannot be stored.")


    def retrieve_asset(self, name):
        asset, loc = self.scan(name, 'rig')
        if asset is None:
            print(f"{asset} not found in rig storage.")
        else:
            if not asset.get_encrypted():
                if self.__trace_level < 5:
                    self.__rig.retrieve_asset(asset)
                    self.__inventory.append(asset)
                    self.increase_trace_level()
                else:
                    print("Trace level is too high.")
            elif asset.get_encrypted() == True:
                print(f"{asset} is encrypted and cannot be retrieved.")



    def scan(self, name, loc = 'both'):
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
        new_asset = Asset(asset, None)
        if loc == 'inventory':
            self.__inventory.append(new_asset)
        elif loc == 'rig':
            self.__rig.store_asset(new_asset)
        print(f"{asset} added to {loc}.")

    def remove_asset(self, asset, loc='inventory'):
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
        if self.__trace_level > 4:
            print(f"Trace level maxxed out, wait to cool down.")
        else:
            self.__trace_level += 1
            print(f"Trace level increased to {self.__trace_level}.")

    def reduce_trace_level(self):
        if self.__trace_level == 0:
            return
        self.__trace_level -= 1
        print(f"Trace level reduced to {self.__trace_level}.")

    def asset_gen(self):
        self.__rig.asset_gen()
        return
