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
    letter_list = []

    def create_list_name(self):
        global list_name
        list_name = []
        for i in self.context.driver.find_elements_by_css_selector('a.name'):
            list_name.append(i.text)
        return list_name

    def create_alphabet(self):
        global alphabet
        alphabet = []
        for i in self.context.driver.find_elements_by_css_selector('li>a.pagination-item'):
            alphabet.append(i.text)
        return alphabet

    def choose_letter(self):
        global letter_list
        global rletter
        rletter = self.create_alphabet()[random.randint(0, len(self.create_alphabet()) - 1)]
        xpath = "//a[@class='pagination-item'][text()='" + rletter + "']"
        self.context.driver.find_element_by_xpath(xpath).click()
        letter_list = self.create_list_name()

    def compare_list(self):
        if any(item.startswith(self.rletter) for item in self.list_name) == (self.letter_list):
            return 1
        else:
            return 0
