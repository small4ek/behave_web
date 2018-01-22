# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we are on Account Page')
def step_impl(context):
    context.settings_page.navigate()


@when('we click API access')
def step_impl(context):
    context.settings_page.api_access()
    assert '/confirm_password?redirect_to=/account/api' in context.settings_page.current_url()


@when('we reenter password')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass)
    context.settings_page.api_submit()
    assert '/account/api' in context.settings_page.current_url()


@then('we are on API access page')
def step_impl(context):
    context.api_page.navigate()


@when('we create new API token')
def step_impl(context):
    context.api_page.create_new_token()


@then('we see new API token')
def step_impl(context):
    context.api_page.check_token()
