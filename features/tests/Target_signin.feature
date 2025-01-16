# Created by BCC at 11/24/2024
Feature: Test for signing in
  # Enter feature description here

  Scenario: User is taken to sign in page
  Given Open Target main page
  When Click Sign In
  When From right side navigation menu, click Sign In
  Then Verify Sign In form opened

  Scenario: User gets message after incorrect credentials
    Given Open sign in page
    When Enters incorrect email and password combination
    And Clicks login button
    Then Verify that “We can't find your account” message is shown

    # Enter steps here