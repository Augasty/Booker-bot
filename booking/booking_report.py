# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement 
from selenium.webdriver.common.by import By



class BookingReport:
    
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element

        # self.deal_boxes contains a list of every hotel box.
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        # self.boxes_section_element contains the element inside which all the individual hotel boxes are
        # and this function returns a list of every hotel box from the aforementioned element.
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR, 
        value='div[data-testid="property-card"]'
        )


    def pull_hotel_details(self):
        # this function pulls out the title of every item in the self.deal_boxes. 
        hotel_data_collection = []

        for deal_box in self.deal_boxes:


# hotel_name working fine
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR, value = 'div[data-testid="title"]'
                ).get_attribute('innerHTML').strip()
            print(hotel_name)

# need to see how to make hotel_price and hotel_score work
            # hotel_price = deal_box.find_element(
            #     By.CLASS_NAME, value = 'bui-price-display__value'
            # ).get_attribute('innerHTML').strip()

            # hotel_score = deal_box.find_element(
            #     By.CSS_SELECTOR, value='div[class="b5cd09854e d10a6220b4"]'
            #     ).get_attribute('innerHTML').strip()

            hotel_data_collection.append(
                [hotel_name]
            )

        return hotel_data_collection