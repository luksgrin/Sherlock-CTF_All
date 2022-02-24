# Se ha de ejecutar primero: brownie console --network sherlockctf
from brownie import *

Setup.deploy({'from':accounts[0]})
inflation_instance = Inflation.at(Setup[0].instance())
token_instance = InflationaryToken.at(Inflation.at(Setup[0].instance()).tokenAddress())
