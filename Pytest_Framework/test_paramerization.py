import pytest

from Pytest_Framework.conftest import browser

pytest.mark.usefixtures(browser)
class hub():