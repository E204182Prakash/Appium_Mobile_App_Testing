from time import sleep

def test_open_clock(driver):
    driver.start_activity("com.google.android.deskclock", "com.android.deskclock.DeskClock")
    sleep(2)
    # Just assert that activity is clock
    assert "deskclock" in driver.current_package