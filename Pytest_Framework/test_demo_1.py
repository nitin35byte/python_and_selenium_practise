import pytest
@pytest.mark.skip
def test_firstprogram5(setup):
    print("hello")
@pytest.mark.usefixtures("setup")
class TestExmaple:

    def test_firstprogram1(self):
        print("hello")

    def test_firstprogram2(self):
        print("hello")


    def test_firstprogram3(self):
        print("hello")


    def test_firstprogram4(self):
        print("hello")


    def test_firstprogram(setup):
        print("hello")

