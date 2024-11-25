# Created by archanamalik at 11/23/24
Feature: Tests for search
  # Enter feature description here

  Scenario: User can successfully navigate to  signin
    Given Open target main page
    When Click Sign In
    Then Verify Sign In form opened

  Scenario: To verifies that your cart is empty
    Given Open target main page
    When Click on cart icon
    Then Verify that cart is empty

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown
  # Enter steps here

