def test_amm_faucet(amm):
    """
    Test if the faucet correctly initializes the token1 and token2 holdings
    """
    amm.faucet(10, 15)
    holdings = amm.getMyHoldings()

    assert holdings[0] == 10
    assert holdings[1] == 15
    assert holdings[2] == 0
