from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import booking.constants as const
import time
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport


class Booking(webdriver.Firefox):
    def __init__(self, teardown = False):
        self.teardown = teardown

        super().__init__()
        # here self is the driver
        self.implicitly_wait(30)
        self.maximize_window()

    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)


        # to stop the test from ending
        # and closing the browser. ... only needed for chrome
        # while True:
        #     pass

    
    def change_currency(self,currency=None):
        currency_element = self.find_element(By.CSS_SELECTOR, value='button[data-tooltip-text="Choose your currency"]')
        currency_element.click()

        selected_currency_element = self.find_element(By.CSS_SELECTOR, value = f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        selected_currency_element.click()


    def select_place_to_go(self,place_to_go):
        search_field = self.find_element(By.ID, value="ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(3)
        search_field.send_keys(Keys.BACK_SPACE)

        
        find_result = self.find_element(By.CSS_SELECTOR, value='li[data-i="0"]')
        find_result.click()


    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR, value = f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR, value = f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()


    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, value = 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR, value = 'button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            # if  value of adult == 1
            # we will go out of the while loop
            adults_value_element = self.find_element(By.ID, value="group_adults")

            # this function retrives the value attribute from adults_value_element
            # and stores it in the adults_value variable
            adults_value = adults_value_element.get_attribute('value')
            if int(adults_value) == 1:
                break
        
        increase_button_element = self.find_element(By.CSS_SELECTOR, value = 'button[aria-label="Increase number of Adults"]')

        for _ in range(count - 1):
            increase_button_element.click()


    
    def click_search(self):
        search_button = self.find_element( By.CSS_SELECTOR,value = 'button[type="submit"]')
        search_button.click()




    def apply_filtration(self,):
        filtration = BookingFiltration(driver = self)
        filtration.apply_star_rating(4,5)

        time.sleep(5)  #giving the time to let the page load after filtration
        filtration.sort_by_price()


    def report_results(self):
        # time.sleep(5)

        # hotel_boxes contains the element inside which all the individual hotel boxes are
        hotel_boxes = self.find_element(By.CSS_SELECTOR, value = 'div[class="d4924c9e74"]')
        report = BookingReport(hotel_boxes)
        
        print(report.pull_hotel_details())