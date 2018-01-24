# -*- coding: UTF-8 -*-
from .base_page import Page


class ApiPage(Page):
    """
    Start page for API access
    """

    url = '/account/api'

    def create_new_token(self, token_name):
        self.context.driver.find_element_by_id('label').click()
        self.context.driver.find_element_by_id('label').send_keys(token_name)
        self.context.driver.find_element_by_id('create').click()


    def check_token_by_name(self, token_name):
        for i in self.context.driver.find_elements_by_css_selector('#tokens tbody  tr.data'):
            if i.find_element_by_css_selector('td span.editable').text == token_name:
                return i.find_element_by_css_selector('td.token').text


    def delete_token_by_name(self, token_name):
        for i in self.context.driver.find_elements_by_css_selector('#tokens tbody  tr.data'):

            if i.find_element_by_css_selector('td span.editable').text == token_name:
                i.find_element_by_css_selector(' tr.data td form.aui').click()
        alert = self.context.driver.switch_to_alert()
        alert.accept()