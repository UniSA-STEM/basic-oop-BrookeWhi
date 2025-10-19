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
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.")]
        self.__rig = ""
        self.__trace_level = 0

    def __str__(self):
        inventory = self.get_inventory
        return (f"Hacker: {self.__name}, Rig: {self.__rig}, Trace Level: {self.__trace_level}, Inventory: {inventory}")

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def get_inventory_item(self, item):
        for i in self.__inventory:
            if i.get_name() == item:
                return i, "inv"
        for i in self.__rig.get_storage():
            if i.get_name() == item:
                return i, "rig"
        return print('No item found.')

    def consume_asset(self, asset):
        if self.scan(asset, 'inventory') is not None:
            self.__inventory.remove(asset)
            print(f"{asset} consumed from inventory.")
        else:
            print(f"{asset} not found in inventory.")


    def acquire_rig(self):
        if self.scan("CryptoToken", 'inventory') is not None:
            if self.__rig == "":
                self.consume_asset("CryptoToken")
                self.__rig = Rig()
                print(f"{self.__name} has acquired {self.__rig.name}")
            else:
                print("Hacker already has a rig.")

    def get_rig(self):
        return self.__rig

    def use_asset(self, asset, target=None):
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
                self.consume_asset("Data Spike")
                target.__rig.take_damage()
            else:
                print("Need Data Spike.")
        # Hardware Patch
        elif asset.name == "Hardware Patch":
            if self.scan("Hardware Patch", 'inventory') is not None:
                self.consume_asset("Hardware Patch")
                self.__rig.upgrade_rig(self)
            else:
                print("Need Hardware Patch.")

        # Removable Drive
        elif asset.name == "Removable Drive":
            if self.scan("Removable Drive", 'inventory') is not None:
                if target is not None:
                    target_rig = target.__rig
                    if target_rig is not None:
                        target_rig.extract_assets(self)
                        self.consume_asset("Removable Drive")
                    else:
                        print("Target has no rig.")
                else:
                    print("No target specified for extraction.")
            else:
                print("Need Removable Drive.")

        # Security Chip
        elif asset.name == "Security Chip":
            if self.scan("Security Chip", 'inventory') is not None:
                self.consume_asset("Security Chip")
                if asset.__encrypted == False:
                    self.encrypt_asset(asset)
                elif asset.__encrypted == True:
                    self.decrypt_asset(asset)
            else:
                print("Need Security Chip.")

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

    
    def encrypt_asset(self, asset):
        if self.get_inventory_item("Security Chip"):
            self.consume_asset("Security Chip")
            Asset.encrypt(asset)

    def decrypt_asset(self, asset):
        if self.get_inventory_item("Security Chip"):
            self.consume_asset("Security Chip")
            Asset.decrypt(asset)
        else:
            print("No Security Chip")

    def store_asset(self, asset):
        if self.scan(asset, 'inventory') is not None:
            if asset.__encrypted == False:
                self.__rig.store_asset(asset)
                self.__inventory.remove(asset)

            elif asset.__encrypted == True:
                print(f"{asset} is encrypted and cannot be stored.")
        else:
            print(f"{asset} not found in inventory.")

    def retrieve_asset(self, asset):
        if self.scan(asset, 'rig') is not None:
            if asset.__encrypted == False:
                self.__rig.retrieve_asset(asset)
                self.__inventory.append(asset)
            elif asset.__encrypted == True:
                print(f"{asset} is encrypted and cannot be retrieved.")
        else:
            print(f"{asset} not found in rig storage.")


    def scan(self, name, loc = 'both'):
        if loc in ('both', 'inventory'):
            for i in self.__inventory:
                if i.name == name:
                    return i, 'inventory'
        if loc in ('both', 'rig'):
            for i in self.__rig.get_storage():
                if i.name == name:
                    return i, 'rig'
        return None

