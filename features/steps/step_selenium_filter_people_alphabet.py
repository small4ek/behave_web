# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------

from behave import given, when, then


@given('we are on Authorized Page')
def step_impl(context):
    context.authorized_page.navigate()


@when('we click People')
def step_impl(context):
    context.authorized_page.switch_to_people()


@then('we are on People Page')
def step_impl(context):
    context.people_page.navigate()


@when('we choose a letter')
def step_impl(context):
    pass


@then('we see users profiles start at letter')
def step_impl(context):
    pass
