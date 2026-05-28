Feature: Social links
  Tests that social links navigate to the correct destinations

  Scenario: Twitter link opens correct page
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I open the Twitter social link
    Then I should be on the Twitter page

  Scenario: Facebook link opens correct page
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I open the Facebook social link
    Then I should be on the Facebook page

  Scenario: LinkedIn link opens correct page
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I open the LinkedIn social link
    Then I should be on the LinkedIn page
