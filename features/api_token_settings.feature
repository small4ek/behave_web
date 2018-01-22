Feature: Checking account settings

Scenario: Check account settings

   Given we are on Hipchat Home Page
    When we edit profile
    Then we click API access
    When we reenter password
    Then we are on API access page