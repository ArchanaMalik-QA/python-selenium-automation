# Created by archanamalik at 12/9/24
Feature: Tests for Target Circle Page

  Scenario: User can see 10 benefit cells
    Given Open target circle page
    Then Verify at least 10 benefit cells
