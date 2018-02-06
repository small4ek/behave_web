# -*- coding: UTF-8 -*-
from selenium.webdriver.common.keys import Keys

from .base_page import Page
import  random

class PeoplePage(Page):
    """
    Start page for People profiles
    """

    url = '/people'
    list_name = []
    rletter = ''

    def create_list_name(self):
        list_name = []
        for i in self.context.driver.find_elements_by_css_selector('a.name'):
            list_name.append(i.text)
        return list_name

    def set_list_name(self):
        self.list_name = self.create_list_name()

    def create_alphabet(self):
        alphabet = []
        for i in self.context.driver.find_elements_by_css_selector('li>a.pagination-item'):
            alphabet.append(i.text)
        return alphabet

    def choose_letter(self):
        self.rletter = self.create_alphabet()[random.randint(0, len(self.create_alphabet()) - 1)]
        xpath = "//a[@class='pagination-item'][text()='" + self.rletter + "']"
        self.context.driver.find_element_by_xpath(xpath).click()

    def compare_list(self):
        letter_list = self.create_list_name()
        if any(item.startswith(self.rletter) for item in self.list_name) == letter_list:
            return 1
        else:
            return 0
