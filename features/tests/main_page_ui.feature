# Created by archanamalik at 12/9/24
Feature: Tests for Main page UI

  Scenario: Verify that logged out user can access Sign In
    Given Open target main page
    When Click on Signin icon
    And User click on Signin Button
    Then Verify Sign In form opened

  Scenario: User can see header links
    Given Open target main page
    Then Verify at least 1 header link is shown

  Scenario: User can see correct amount of header links
    Given Open target main page
    Then Verify 6 header links are shown