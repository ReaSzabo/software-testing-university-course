Feature: Saucedemo about link
  Tests navigation to the Saucelabs website via the menu

  Scenario: Open About page
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I open the About page
    Then I should be on the Saucelabs website
