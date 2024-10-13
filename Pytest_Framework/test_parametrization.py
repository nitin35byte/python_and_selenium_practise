import pytest


@pytest.fixture(params=["chrome",'firefox','edge'])
def cross_browser(request):
    return request.params