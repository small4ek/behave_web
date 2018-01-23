# -*- coding: UTF-8 -*-
"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

"""

from selenium import webdriver

from features.environment_secret import HIPCHAT_LOGIN, HIPCHAT_PASS
from pages.login_page import LoginPage
from pages.authorized_page import AuthorizedPage
from pages.api_page import ApiPage
from pages.settings_page import SettingsPage
import selenium.webdriver.support.ui as ui

def before_all(context):
    context.hipchat_login = HIPCHAT_LOGIN
    context.hipchat_pass = HIPCHAT_PASS
    context.base_url = "https://bortnik.hipchat.com"
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context)
    context.authorized_page = AuthorizedPage(context)
    context.api_page = ApiPage(context)
    context.settings_page = SettingsPage(context)
    context.wait = ui.WebDriverWait(context.driver, 10)

def after_all(context):
    context.driver.quit()
