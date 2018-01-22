# -*- coding: UTF-8 -*-

from .base_page import Page


class ApiPage(Page):
    """
    Start page for API access
    """

    url = '/account/api'

    def create_new_token(self):
        self.context.driver.find_element_by_id('label').click()
        self.context.driver.find_element_by_id('label').send_keys('test')
        self.context.driver.find_element_by_id('create').click()

    def check_token(self):
        ch_token = self.context.driver.find_element_by_id('label').get_attribute('value')
        if len(ch_token) > 0:
            return True
        else:
            return False
