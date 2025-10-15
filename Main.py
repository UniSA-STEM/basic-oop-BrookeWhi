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

# ## Testing

z = Hacker("Z")
print(z._Hacker__inventory)
r = Rig("toob")
print(r._Rig__storage)
r.assetGen()
print(r._Rig__storage)
print(r._Rig__broken_state)
r.repair(z)
print(r._Rig__broken_state)
print(z._Hacker__inventory)
a = r._Rig__storage[2]
z.acquire_rig("toob")
print(z._Hacker__rig)
print(z.__str__())
print(r.__str__())
print(a.__str__())