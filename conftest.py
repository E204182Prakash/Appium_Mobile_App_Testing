import pytest
from appium import webdriver
from time import sleep

@pytest.fixture
def driver(request):
    caps = {
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "emulator-5554",
        "automationName": "UiAutomator2",
        "noReset": True
    }
    driver = webdriver.Remote("http://127.0.0.1:4723", caps)
    sleep(2)
    yield driver
    driver.quit()
