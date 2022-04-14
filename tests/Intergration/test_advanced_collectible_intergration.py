from tarfile import BLOCKSIZE
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from brownie import network
import pytest
from scripts.Simple_Collectible.deploy_and_create import deploy_and_create
from scripts.Advanced_Collectible.deploy_and_create import deploy_and_create
import time


def test_can_create_advanced_collectible_intergration():
    # deploy the contract
    # create an NFT
    # get a random breed back
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    # Act
    advanced_collectible, creation_transaction = deploy_and_create()
    time.sleep(60)
   
    #Assert
    assert advanced_collectible.tokenCounter() == 1
    