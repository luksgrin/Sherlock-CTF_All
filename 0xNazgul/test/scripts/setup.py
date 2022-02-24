from brownie import *

# Deploy
Setup.deploy({'from': accounts[0], 'amount':'1 ether'})

# Get instance
FloraToken.at(Setup[0].instance())
