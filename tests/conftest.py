import pytest


@pytest.fixture(autouse=True)
def setup(fn_isolation):
    """
    Isolation setup fixture.
    This ensures that each test runs against the same base environment.
    """
    pass


@pytest.fixture(scope="module")
def amm(accounts, AMM):
    """
    Yield a `Contract` object for the AMM contract.
    """
    yield AMM.deploy({"from": accounts[0]})
