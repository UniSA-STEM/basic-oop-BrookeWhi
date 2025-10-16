"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs."), Asset("Security Chip", "Used to encrypt or decrypt."), Asset("Security Chip", "Used to encrypt or decrypt.")]
        self.__rig = ""
        self.__trace_level = 0

    def get_inventory(self):
        return self.__inventory

    def get_inventory_item(self, item):
        for i in self.__inventory:
            if i.get_name() == item:
                return i
        return print('No item found.')

    def consume_asset(self, asset):
        if asset in self.__inventory:
            self.__inventory.remove(asset)

    def acquire_rig(self, rig):
        self.__rig = rig

    # def launch_spike(self, target_rig):
    # def extract_assets(self, target_rig):
    #
    
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

    # def store_asset(self, asset):
    #
    # def retrieve_asset(self, asset):
    #
    # def scan_asset(self, asset):

    def __str__(self):
        inventory = self.__inventory
        return (f"Hacker: {self.__name}, Rig: {self.__rig}, Trace Level: {self.__trace_level}, Inventory: {inventory}")