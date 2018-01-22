Feature: Checking account settings


  Background:
    Given we are on API access Page


Scenario: Check create new API token

    When we create new API token
    Then we see new API token