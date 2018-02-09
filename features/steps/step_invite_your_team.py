from behave import when, given, then

@when('we click "{text}"')
def step_impl(context, text):
    context.lobby_page.invite_team_form(text)

@when('we click on hint icon')
def step_impl(context):
    context.lobby_page.invite_team_help_form()


@when('we add the emails')
def step_impl(context):
    context.lobby_page.invite_team_email_input()


@when('we delete one email')
def step_impl(context):
    context.lobby_page.delete_email_from_list()


@when('we send invite')
def step_impl(context):
    context.lobby_page.click_send_invite()


@then('we see success message')
def step_impl(context):
    assert 'Invites sent' in context.lobby_page.success_invite_message()





