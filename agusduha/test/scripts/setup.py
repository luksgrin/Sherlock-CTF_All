from brownie import *

# Deploy
Setup.deploy({'from': accounts[0], 'amount':'0.2 ether'})

# Get instance
KingVault.at(Setup[0].instance())
