#!/usr/bin/python3
from brownie import APIConsumer, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    get_contract,
)


from brownie import PriceExercise, config, network
from scripts.helpful_scripts import (
    get_account,
    get_verify_status,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
 
 
 
def deploy_price_exercise():
    jobId = config["networks"][network.show_active()]["jobId"]
    fee = config["networks"][network.show_active()]["fee"]
    account = get_account()
    price_exercise = PriceExercise.deploy(
        get_contract("oracle").address,
        jobId,
        fee,
        get_contract("link_token").address,
        get_contract("btc_usd_price_feed").address,
        {"from": account},
        publish_source=get_verify_status(),
    )
    print(f"Price Exercise deployed to {price_exercise.address}")
    return price_exercise
 
 
def main():
    deploy_price_exercise()
