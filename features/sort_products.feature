Feature: Products sorting
  Tests that products are sorted correctly using the available filters

  Scenario Outline: Products can be sorted by different filters
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I sort products by "<sort>"
    Then the products should be sorted "<sort>"

    Examples:
      | sort |
      | az   |
      | za   |
      | lohi |
      | hilo |
