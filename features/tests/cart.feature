# Created by archanamalik at 12/9/24
Feature: Tests for cart functionality

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty ' message is shown

  @smoke
  Scenario: User can add a product to cart
    Given Open target main page
    When Search for Pan
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product