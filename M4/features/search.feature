Feature: search flipkart
  Scenario Outline: search data
    Given We are on flipkart website
    When Validate logi
    Then Enter your "<username>" in the feild
    And Enter your "<password>" in the box
    And click login
    Then Click of the search bar
    And Click on search button
    Then Check on Relevance is clickable
    Then Check on popularity is clickable
    Then Check on Price low-high is clickable
    Then Check on Price high-low is clickable
    Then Check on newest first is clickable

    Examples:
      |  |