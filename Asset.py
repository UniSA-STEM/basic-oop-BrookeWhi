"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
Assets = {
        "CryptoToken": {"description": "Used to acquire or repair rigs."},
        "Data Spike": {"description": "Used in battles."},
        "Removable Drive": {"description": "Found in rigs and used for extraction."},
        "Security Chip": {"description": "Used to encrypt or decrypt."},
        "Hardware Patch": {"description": "Used to upgrade rigs."}
    }
class Asset:
    def __init__(self, name, description = None):
        self.name = name
        self.__name = self.name
        self.description = Assets[name]["description"] if description is None else description
        self.__description = self.description
        self.__encrypted = False

    def __str__(self):
        if self.get_encrypted() == True:
            return (f"Asset: {self.__name}: {self.__description} [Encrypted]")
        else:
            return (f"Asset: {self.__name}: {self.__description}")

    def encrypt(self):
        print(self)
        if self.__encrypted == False:
            self.__encrypted = True
            print(f"{self.__name} now encrypted")
        else:
            print(f"{self.__name} already encrypted")

    def decrypt(self):
        if self.__encrypted == True:
            self.__encrypted = False
            print(f"{self.__name} now decrypted")
        else:
            print(f"{self.__name} cannot be decrypted")

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted

