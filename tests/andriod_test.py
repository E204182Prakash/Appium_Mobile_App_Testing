from appium import webdriver
from time import sleep

# Desired capabilities for the Clock app
desired_caps = {
    "platformName": "Android",
    "platformVersion": "12",
    "deviceName": "emulator-5554",
    "automationName": "UiAutomator2",
    "appPackage": "com.google.android.deskclock",
    "appActivity": "com.android.deskclock.DeskClock",
    "noReset": True
}

# Connect to Appium server
driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

# Wait for app to load
sleep(3)

# Click the "+" button to add a new alarm (example XPath, may vary)
driver.find_element("accessibility id", "Add alarm").click()
sleep(2)

# Set hour to 7 and minute to 30 (example: adjust according to your emulator layout)
driver.find_element("id", "com.google.android.deskclock:id/digital_clock_hour").send_keys("7")
driver.find_element("id", "com.google.android.deskclock:id/digital_clock_minute").send_keys("30")

# Save the alarm (example: may need to adjust XPath or id)
driver.find_element("id", "com.google.android.deskclock:id/fab").click()

# Wait to see the result
sleep(3)

# Close the session
driver.quit()
