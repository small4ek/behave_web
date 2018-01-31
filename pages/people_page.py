# -*- coding: UTF-8 -*-
from selenium.webdriver.common.keys import Keys

from .base_page import Page
import  random

class PeoplePage(Page):
    """
    Start page for People profiles
    """

    url = '/people'


    def create_list_name(self):
        list_name = []
        for i in self.context.driver.find_elements_by_css_selector('a.name'):
                list_name.append(i.text)
                #print(list_name)

    def choose_letter(self):
        alphabet = []
        for i in self.context.driver.find_elements_by_css_selector('li>a.pagination-item'):
            alphabet.append(i.text)
        rletter = alphabet[random.randint(0, len(alphabet) - 1)]
        xpath = "//a[@class='pagination-item'][text()='" + rletter + "']"
        self.context.driver.find_element_by_xpath(xpath).click()
        letter_list = self.create_list_name()
        #print(letter_list)


    def compare_list(self):
        #pass
        if any(item.startswith(self.choose_letter().rletter) for item in self.create_list_name().list_name) == self.choose_letter().letter_list:
            return 1
        else:
            return 0