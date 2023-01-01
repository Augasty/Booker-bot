#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    # typing
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, value = 'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR,value='*')


        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()


    def sort_by_price(self):
        self.driver.find_element(By.CSS_SELECTOR, value='span[class="cb5ebe3ffb"]').click()

        lowest_first = self.driver.find_element(By.CSS_SELECTOR, value='button[data-id="price"]')
        lowest_first.click()