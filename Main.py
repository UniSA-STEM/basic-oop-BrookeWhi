"""
File: main.py
Description: <A brief description of this Python module.>
Author: Brooke Whitmore
ID: 110468647
Username: BrookeWhi
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Rig import Rig
from Asset import Asset

HACKER = None
HACKER_NAME = "S1CKVYGS"


TARGET_HACKER = None
TARGET_HACKER_NAME = "TH3BUTCH3R"

def create_hacker_instances():
    global HACKER, TARGET_HACKER
    HACKER = Hacker(HACKER_NAME)
    if HACKER is not None:
        print(f"Hacker {HACKER_NAME} has been created!")

    TARGET_HACKER = Hacker(TARGET_HACKER_NAME)
    if TARGET_HACKER is not None:
        print(f"Hacker {TARGET_HACKER_NAME} has been created!")

    return HACKER, TARGET_HACKER


print("---------------------------------------------")
print("Running: create_hacker_instances()")
print("---------------------------------------------")
create_hacker_instances()
print("---------------------------------------------")


def create_rig_instances():
    HACKER.acquire_rig()
    TARGET_HACKER.acquire_rig()


print("\n---------------------------------------------")
print("Running: create_rig_instances()")
print("---------------------------------------------")
create_rig_instances()
print("---------------------------------------------")


def hacker_acquire_rig_without_token():
    HACKER = Hacker(HACKER_NAME)
    if HACKER is not None:
        print(f"Hacker {HACKER_NAME} has been created!")
    HACKER.remove_asset("CryptoToken")
    HACKER.acquire_rig()


print("\n---------------------------------------------")
print("Running: hacker_acquire_rig_without_token()")
print("---------------------------------------------")
hacker_acquire_rig_without_token()

def hacker_acquire_rig_with_existing_rig():
    HACKER = Hacker(HACKER_NAME)
    if HACKER is not None:
        print(f"Hacker {HACKER_NAME} has been created!")
    HACKER.acquire_rig()
    HACKER.add_asset("CryptoToken")
    HACKER.acquire_rig()


print("\n---------------------------------------------")
print("Running: hacker_acquire_rig_with_existing_rig()")
print("---------------------------------------------")
hacker_acquire_rig_with_existing_rig()


def print_current_states():
    print(HACKER.__str__())
    print(HACKER.get_rig().__str__())



print("\n---------------------------------------------")
print("Running: print_current_states()")
print("---------------------------------------------")
print_current_states()
print("---------------------------------------------")


def hacker_upgrade_rig():
    HACKER.add_asset("Hardware Patch")
    HACKER.use_asset("Hardware Patch")


print("\n---------------------------------------------")
print("Running: hacker_upgrade_rig()")
print("---------------------------------------------")
hacker_upgrade_rig()
print("---------------------------------------------")


def hacker_upgrade_rig_without_patch():
    HACKER = Hacker(HACKER_NAME)
    HACKER.acquire_rig()
    HACKER.use_asset("Hardware Patch")


print("\n---------------------------------------------")
print("Running: hacker_upgrade_rig_without_patch()")
print("---------------------------------------------")
hacker_upgrade_rig_without_patch()
print("---------------------------------------------")


def hacker_upgrade_rig_without_rig():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.add_asset("Hardware Patch")
    TEST_HACKER.use_asset("Hardware Patch")


print("\n---------------------------------------------")
print("Running: hacker_upgrade_rig_without_rig()")
print("---------------------------------------------")
hacker_upgrade_rig_without_rig()
print("---------------------------------------------")


def hacker_upgrade_rig_at_max_level():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    for _ in range(4):
        TEST_HACKER.add_asset("Hardware Patch")
        TEST_HACKER.use_asset("Hardware Patch")



print("\n---------------------------------------------")
print("Running: hacker_upgrade_rig_at_max_level()")
print("---------------------------------------------")
hacker_upgrade_rig_at_max_level()
print("---------------------------------------------")


def hacker_encrypt_asset():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.add_asset("Security Chip", 'inventory')
    TEST_HACKER.use_asset('Security Chip', 'Data Spike')


print("\n---------------------------------------------")
print("Running: hacker_encrypt_asset()")
print("---------------------------------------------")
hacker_encrypt_asset()
print("---------------------------------------------")


def hacker_encrypt_asset_without_security_chip():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.use_asset('Security Chip')


print("\n---------------------------------------------")
print("Running: hacker_encrypt_asset_without_security_chip()")
print("---------------------------------------------")
hacker_encrypt_asset_without_security_chip()
print("---------------------------------------------")



def hacker_decrypt_asset():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.add_asset("Security Chip", 'inventory')
    TEST_HACKER.add_asset("Security Chip", 'inventory')
    TEST_HACKER.add_asset("Data Spike", 'inventory')
    TEST_HACKER.use_asset('Security Chip', 'Data Spike')
    TEST_HACKER.use_asset('Security Chip', 'Data Spike')

print("\n---------------------------------------------")
print("Running: hacker_decrypt_asset()")
print("---------------------------------------------")
hacker_decrypt_asset()
print("---------------------------------------------")

def hacker_decrypt_asset_without_security_chip():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.use_asset('Security Chip', 'Data Spike')



print("\n---------------------------------------------")
print("Running: hacker_decrypt_asset_without_security_chip()")
print("---------------------------------------------")
hacker_decrypt_asset_without_security_chip()
print("---------------------------------------------")

def hacker_retrieve_asset():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.retrieve_asset("Data Spike")


print("\n---------------------------------------------")
print("Running: hacker_retrieve_asset()")
print("---------------------------------------------")
hacker_retrieve_asset()
print("---------------------------------------------")

def hacker_store_asset():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.add_asset("Hardware Patch", 'inventory')
    TEST_HACKER.store_asset("Hardware Patch")

print("\n---------------------------------------------")
print("Running: hacker_store_asset()")
print("---------------------------------------------")
hacker_store_asset()
print("---------------------------------------------")

def hacker_store_encrypted_asset():
    TEST_HACKER = Hacker(HACKER_NAME)
    TEST_HACKER.acquire_rig()
    TEST_HACKER.add_asset("Hardware Patch", 'inventory')
    TEST_HACKER.add_asset("Security Chip", 'inventory')
    TEST_HACKER.use_asset('Security Chip', 'Hardware Patch')
    TEST_HACKER.store_asset("Hardware Patch")

print("\n---------------------------------------------")
print("Running: hacker_store_encrypted_asset()")
print("---------------------------------------------")
hacker_store_encrypted_asset()
print("---------------------------------------------")

def hacker_launch_attack():
    HACKER = Hacker("S1CKVYGS")
    HACKER.acquire_rig()
    TARGET_HACKER = Hacker('T4RG3T_H4KK3R')
    TARGET_HACKER.acquire_rig()
    TARGET_HACKER.add_asset("Security Chip", 'inventory')
    TARGET_HACKER.use_asset('Security Chip', 'Removable Drive')
    HACKER.retrieve_asset("Data Spike")
    HACKER.retrieve_asset("Data Spike")
    HACKER.use_asset("Data Spike", TARGET_HACKER)
    HACKER.use_asset("Data Spike", TARGET_HACKER)
    HACKER.retrieve_asset("Removable Drive")
    HACKER.use_asset("Removable Drive", TARGET_HACKER)

print("\n---------------------------------------------")
print("Running: hacker_store_encrypted_asset()")
print("---------------------------------------------")
hacker_launch_attack()
print("---------------------------------------------")


def hacker_launch_attack_over_trace():
    HACKER = Hacker("S1CKVYGS")
    HACKER.acquire_rig()
    TARGET_HACKER = Hacker('T4RG3T_H4KK3R')
    TARGET_HACKER.acquire_rig()
    HACKER.retrieve_asset("Data Spike")
    HACKER.retrieve_asset("Data Spike")
    HACKER.use_asset("Data Spike", TARGET_HACKER)
    TARGET_HACKER.asset_gen()
    HACKER.retrieve_asset("Removable Drive")
    HACKER.use_asset("Removable Drive", TARGET_HACKER)
    HACKER.use_asset("Data Spike", TARGET_HACKER)
    TARGET_HACKER.asset_gen()
    HACKER.use_asset("Removable Drive", TARGET_HACKER)
    HACKER.reduce_trace_level()


print("\n---------------------------------------------")
print("Running: hacker_launch_attack_over_trace()")
print("---------------------------------------------")
hacker_launch_attack_over_trace()
print("---------------------------------------------")















