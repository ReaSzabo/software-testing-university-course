Feature: Saucedemo logout
  Tests logout functionality from the products page

  Scenario: Logout
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I logout
    Then I should see the login page
