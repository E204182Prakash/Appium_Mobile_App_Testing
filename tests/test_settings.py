from time import sleep

def test_open_settings(driver):
    driver.start_activity("com.android.settings", "com.android.settings.Settings")
    sleep(2)
    assert "settings" in driver.current_package