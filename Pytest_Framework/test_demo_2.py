import pytest

@pytest.mark.xfail
def test_credit_card():
    print("hello")

@pytest.fixture()
def setup():
    print("I will execute firrts")

def test_fixtures(setup):
    print("I will execute steps in fixtures demo")


def test_crossbrowser(browser):
    print(browser)
