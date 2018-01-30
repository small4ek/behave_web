# -*- coding: UTF-8 -*-
from selenium.webdriver.common.keys import Keys

from .base_page import Page


class PeoplePage(Page):
    """
    Start page for People profiles
    """

    url = '/people'


    # def create_new_token(self):
    #     self.context.driver.find_element_by_id('label').click()
    #     self.context.driver.find_element_by_id('label').send_keys('test')
    #     self.context.driver.find_element_by_id('create').click()

    def create_list_name(self):
        list_name = []
        for i in self.context.driver.find_elements_by_css_selector('a.name'):
                list_name.append(i.text)

    def create_alphabet(self):
        alphabet = []
        for i in self.context.driver.find_elements_by_css_selector('li>a.pagination-item'):
            if i == "All" or "Other":
                pass
            else:
                alphabet.append(i.text)

