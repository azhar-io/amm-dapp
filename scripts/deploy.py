from brownie import accounts, network, AMM


def deploy_amm_dev():
    # uses default brownie accounts
    owner = accounts[0]
    AMM.deploy({'from': accounts[0]})


def main():
    if network.show_active() == 'development':
        deploy_amm_dev()
