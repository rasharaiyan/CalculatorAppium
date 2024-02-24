from appium.webdriver.common.by import By

class CalcPage:

    def __init__(self,driver):
        self.driver = driver
        self.__init_app_page()
    def click_button(self, button):
        button_element = self.driver.find_element(By.ID, f"com.google.android.calculator:id/{button.lower()}")
        #.lower() method is used to convert the button identifier to lowercase.
        # By.ID to locate the element by its ID
        button_element.click()


    def add_numbers(self, first_num, second_num):
        self.click_button(first_num)
        self.click_button('PLUS')
        self.click_button(second_num)
        self.click_button('EQUALS')

    def subtract_numbers(self, first_num, second_num):
        self.click_button(first_num)
        self.click_button('MINUS')
        self.click_button(second_num)
        self.click_button('EQUALS')

    def multiply_numbers(self, first_num, second_num):
        self.click_button(first_num)
        self.click_button('MULTIPLE')
        self.click_button(second_num)
        self.click_button('EQUALS')

    def divide_numbers(self, numerator, denominator):
        self.click_button(numerator)
        self.click_button('DIVIDE')
        self.click_button(denominator)
        self.click_button('EQUALS')

    def get_result(self):
        result_element = self.driver.find_element(By.ID, "com.google.android.calculator:id/result_preview")
        return result_element.text