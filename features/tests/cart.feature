# Created by archanamalik at 12/9/24
Feature: Tests for cart functionality

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty ' message is shown

  Scenario: 'Your cart is having added item'
    Given Open target main page
    When Search for tea
    When Add the product to cart
    And Click on Cart icon
    Then Verify 'Your cart is having added items' message is shown


