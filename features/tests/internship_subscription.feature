# Created by BCC at 1/15/2025
Feature: Test for Subscription & payments page
  # Enter feature description here

  Scenario:User can open Subscription & payments page
    Given Open the main page https://soft.reelly.io
    And Log in to the page
    When Click on settings option
    And Click on Subscription & payments option
    Then Verify the right page opens
    And Verify title “Subscription & payments” is visible
    And Verify “back” and “upgrade plan” buttons are available

