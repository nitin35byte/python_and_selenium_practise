import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will execute firrts")

@pytest.fixture()
def dataload():
    print("testdata")
    return["Nitin" ,"Chaudhary","data"]

@pytest.fixture(params=["chrome", "Firefox","IE"])
def browser(request):
    return request.param