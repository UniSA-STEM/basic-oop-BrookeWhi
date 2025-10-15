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
