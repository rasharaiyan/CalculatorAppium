import unittest
from appium import webdriver
from calculator_app import CalcPage
from driver_manager import DriverManager



class TestCalculatorFunctionality(unittest.TestCase):

    def test_addition(self):
        self.calc_page.add_numbers('ONE', 'TWO')
        result = self.calc_page.get_result()
        self.assertEqual(result, "3")

    def test_subtraction(self):
        self.calc_page.subtract_numbers('FIVE', 'TWO')
        result = self.calc_page.get_result()
        self.assertEqual(result, "3")

    def test_multiplication(self):
        self.calc_page.multiply_numbers('THREE', 'FOUR')
        result = self.calc_page.get_result()
        self.assertEqual(result, "12")

    def test_division(self):
        self.calc_page.divide_numbers('NINE', 'THREE')
        result = self.calc_page.get_result()
        self.assertEqual(result, "3")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    driver_manager = DriverManager()
    driver, calc_page = driver_manager.initialize_driver()

    # Run the tests
    unittest.main()

    # Quit the driver after the tests are complete
    driver_manager.quit_driver(driver)
