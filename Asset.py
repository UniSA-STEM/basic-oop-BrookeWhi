"""
File: Asset.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
# Dictionary of all assets
Assets = {
        "CryptoToken": {"description": "Used to acquire or repair rigs."},
        "Data Spike": {"description": "Used in battles."},
        "Removable Drive": {"description": "Found in rigs and used for extraction."},
        "Security Chip": {"description": "Used to encrypt or decrypt."},
        "Hardware Patch": {"description": "Used to upgrade rigs."}
    }
class Asset:
    """
    Class for Asset attributes and functions
    Contains methods for initialising and encryption
    Attributes:
        - name (str): name of the asset
        - description (str): description of the asset
        - encrypted (bool): whether the asset is encrypted
    """

    def __init__(self, name, description = None):
        """
        Constructor of Asset
        :param:
                - name (str): name of the asset
                - description (str): description of the asset
                - encrypted (bool): whether the asset is encrypted
        """
        self.name = name
        self.__name = self.name
        self.description = Assets[name]["description"] if description is None else description
        self.__description = self.description
        self.__encrypted = False

    def __str__(self):
        """
        String conversion method
        :return: (string, string, bool)
        """
        if self.get_encrypted() == True:
            return (f"Asset: {self.__name}: {self.__description} [Encrypted]")
        else:
            return (f"Asset: {self.__name}: {self.__description}")

    def encrypt(self):
        """
        Encrypt asset
        :return: print statement
        """
        # If not encrypted change to encrypted
        if self.__encrypted == False:
            self.__encrypted = True
            print(f"{self.__name} now encrypted")
        else:
            print(f"{self.__name} already encrypted")

    def decrypt(self):
        """
        Decrypt asset
        :return: print statement
        """
        if self.__encrypted == True:
            self.__encrypted = False
            print(f"{self.__name} now decrypted")
        else:
            print(f"{self.__name} cannot be decrypted")

    def get_name(self):
        """
        Get name of asset
        :return: (string)
        """
        return self.__name

    def get_description(self):
        """
        Get description of asset
        :return: (string)
        """
        return self.__description

    def get_encrypted(self):
        """
        Get asset encryption status
        :return: (bool)
        """
        return self.__encrypted

