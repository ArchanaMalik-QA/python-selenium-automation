# Created by archanamalik at 12/21/24
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window


  #Assignment 1 : Lesson 8

  Scenario: User is able to open and close Terms and Conditions from sign in page
    Given Open sign in page
    And Store original window
    When Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close New Window page
    And Return to original window SignIn