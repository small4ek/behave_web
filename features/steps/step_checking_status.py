from behave import when
import time

FULL_NAME = None


@when('we get full user name from settings')
def get_full_name(context):
    global FULL_NAME
    FULL_NAME = context.settings_page.full_name()


@when('we are in chat window')
def step_impl1(context):
    context.lobby_page.navigate()
    time.sleep(6)


@when('we change status for all available cases')
def step_impl(context):
    context.lobby_page.click_dropdown()
    time.sleep(2)
    context.lobby_page.click_away()
    time.sleep(2)
    status_str = context.lobby_page.check_ico(FULL_NAME)
    print(status_str)
    assert 'icon-xa' in status_str
    time.sleep(2)
    context.lobby_page.click_dropdown()
    context.lobby_page.click_do_not_disturb()
    time.sleep(2)
    status_str = context.lobby_page.check_ico(FULL_NAME)
    print(status_str)
    assert 'icon-dnd' in status_str
    time.sleep(2)
    context.lobby_page.click_dropdown()
    context.lobby_page.click_available()
    time.sleep(2)
    status_str = context.lobby_page.check_ico(FULL_NAME)
    print(status_str)
    assert 'icon-avail' in status_str
    time.sleep(2)

