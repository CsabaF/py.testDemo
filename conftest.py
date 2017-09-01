# content of conftest.py
import pytest
import os
import logging

def pytest_addoption(parser):
    parser.addoption("--featureInstance", action="store", default="sprint",
                     help="Feature Instance to run tests on.")

@pytest.fixture
def featureInstance(request):
    instance = request.config.getoption("--featureInstance")
    featureInstance = "https://admin.highwest-" + instance + ".entwinemedia.com"
    return featureInstance

@pytest.fixture(scope='session')
def getBasicAuthKey():
    print(" - Getting Basic authorization Key from system variables.")
    yield os.getenv('ENTWINE_BASIC_AUTHORIZATION_KEY')
    #print("teardown")

@pytest.fixture(scope='session')
def logs():
    logging.basicConfig(level=logging.DEBUG)
    mylogger = logging.getLogger()
    return mylogger