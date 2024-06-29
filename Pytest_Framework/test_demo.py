import pytest

def test_firstprogram(setup):
    msg = "Hello"
    assert msg=="Hello", "If condition not match then test should get fail"

@pytest.mark.smoke
@pytest.mark.skip
def tes_credit_card(setup):
    a = 4
    b = 6
    assert  a+b== 6
