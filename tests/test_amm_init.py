def test_amm_holdings_init(amm):
    """
    Test if the hodlings are correctly intilized to zero
    """
    holdings = amm.getMyHoldings()
    assert holdings[0] == 0
    assert holdings[1] == 0
    assert holdings[2] == 0


def test_amm_pool_init(amm):
    """
    Test if the pool details are intialized correctly
    """

    pool_details = amm.getPoolDetails()
    assert pool_details[0] == 0
    assert pool_details[1] == 0
    assert pool_details[2] == 0

