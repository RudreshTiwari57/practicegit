Feature: search
  Background:
    Given you are on youtube home page
  Scenario: search peaky blinders
    When Validate home page title
    Then Enter peaky blinders
    And hit search button
    Then play video