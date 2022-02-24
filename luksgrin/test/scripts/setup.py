from brownie import *

# Deploy
Setup.deploy({'from': accounts[0], 'amount':'9 ether'})

# Get instance
HauntedDungeon.at(Setup[0].instance())
