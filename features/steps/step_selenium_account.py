# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, then


@given('we are on Account settings Page')
def step_impl(context):
    context.settings_page.navigate()


@then('we see filled account settings')
def step_impl(context):
    assert context.settings_page.check_if_exist(context.settings_page.mention_name(),
                                                context.settings_page.email(),
                                                context.settings_page.full_name())
