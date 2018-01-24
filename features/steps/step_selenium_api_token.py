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

@then('we click Submit')
def step_impl(context):
   context.settings_page.at()
   context.settings_page.api_submit()

@then('we are on API access page')
def step_impl(context):
   #assert context.api_page.at()
   context.settings_page.navigate()

@when('we create new API token')
def step_impl(context):
   context.api_page.create_new_token('test1')


@then('we see new API token')
def step_impl(context):
   context.settings_page.check_if_exist(context.api_page.check_token_by_name('test1'))

