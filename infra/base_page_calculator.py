from appium import webdriver
from calculator_app import CalcPage

class DriverManager:

    def initialize_driver(self):
        capabilities = {
            "platformName": "Android",
            "platformVersion": "13.0",
            "deviceName": "emulator-5554",
            "appPackage": "com.google.android.calculator",
            "appActivity": "com.android.calculator2.Calculator",
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return driver, CalcPage(driver)


    def quit_driver(driver):
        if driver:
            driver.quit()
