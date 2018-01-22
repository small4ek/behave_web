# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we are on API access Page')
def step_impl(context):
    context.api_page.navigate()

@when('we create new API token')
def step_impl(context):
    context.api_page.create_new_token()


@then('we see new API token')
def step_impl(context):
    context.api_page.check_token()


