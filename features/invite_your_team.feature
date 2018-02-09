Feature: Invite your team via email

Scenario: test
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title


Scenario:
    Given we are on Lobby Page
    When we click Invite your team

    And we add the emails
    And we delete one email
    And we send invite
    Then we see success message
