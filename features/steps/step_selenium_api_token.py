# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
import time

@given('we are on Hipchat Home Page')
def step_impl(context):
    context.login_page.navigate()
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    assert "Welcome," in context.authorized_page.get_page_head()


@when('we edit profile')
def step_impl(context):
    context.authorized_page.edit_profile()
    assert '/account' in context.authorized_page.current_url()


@then('we click API access')
def step_impl(context):
    context.authorized_page.api_access()
    assert '/confirm_password?redirect_to=/account/api' in context.authorized_page.current_url()

@when('we reenter password')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass)
    context.authorized_page.api_submit()
    assert '/account/api' in context.authorized_page.current_url()

@then('we are on API access page')
def step_impl(context):
    context.api_page.create_new_token()
    #context.api_page.check_token()

