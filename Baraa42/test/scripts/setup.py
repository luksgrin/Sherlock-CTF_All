from brownie import *

# Deploy
Setup.deploy({'from': accounts[0]})

# Get instance
Casino.at(Setup[0].casino())
