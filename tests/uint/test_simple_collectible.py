from tarfile import BLOCKSIZE
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account
from brownie import network
import pytest
from scripts.Simple_Collectible.deploy_and_create import deploy_and_create
from scripts.Advanced_Collectible.deploy_and_create import deploy_and_create

def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()