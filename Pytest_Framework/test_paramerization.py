import pytest

from Pytest_Framework.conftest import browser

pytest.mark.usefixtures(parm=['Chrome',['Firefox']])
