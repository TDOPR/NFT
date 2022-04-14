from brownie import AdvancedCollectible, accounts
from scripts.helpful_scripts import fund_with_link, get_account
from web3 import Web3

def main():
    account = get_account()
    advanced_collecible = AdvancedCollectible[-1]
    fund_with_link(advanced_collecible, amount = Web3.toWei(0.1, "ether"))
    creation_transaction = advanced_collecible.createCollectible({"from": account})
    creation_transaction.wait(1)
    print("Collectile created!!!")