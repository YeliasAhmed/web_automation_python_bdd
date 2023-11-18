Feature: Google Search

  @search
  Scenario: User searches for a word
    Given user on the google home page
    When the user searches for "Dhaka"
    Then the search results page should be displayed