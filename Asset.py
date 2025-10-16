"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def __str__(self):
        if self.__encrypted == True:
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

    # def assets(self):
    #     return {
    #         "CryptoToken": Asset("CryptoToken", "Used to acquire or repair rigs."),
    #         "Data Spike": Asset("Data Spike", "Used in battles."),
    #         "Removable Drive": Asset("Removable Drive", "Found in rigs and used for extraction."),
    #         "Security Chip": Asset("Security Chip", "Used to encrypt or decrypt."),
    #         "Hardware Patch": Asset("Hardware Patch", "Used to upgrade rigs.")
    #     }