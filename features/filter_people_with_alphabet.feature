
Feature: Checking filtering people with alphabet

Background:
    Given we are on Hipchat Login Page
    When we enter login
    And we enter password
    Then we see Welcome title

Scenario: Check filtering people
    Given we are on Authorized Page
    When we click People
    Then we are on People Page
    When we choose a letter
    Then we see users profiles start at letter
