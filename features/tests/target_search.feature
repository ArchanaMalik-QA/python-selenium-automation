# Created by archanamalik at 11/23/24
Feature: Tests for search
  # Enter feature description here

   Scenario: User can search for tea
    Given Open target main page
    When Search for tea
    Then Verify search results shown for tea
    Then Verify search term tea in URL

  Scenario: User can search for coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown for coffee

  Scenario: User can search for a mug
    Given Open target main page
    When Search for a mug
    Then Verify search results shown for mug

  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for coffeemaker
    Then Verify that every product has a name and an image