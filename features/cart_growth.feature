Feature: Cart item count growth
  Tests how the cart badge count increases as items are added

  Scenario Outline: Cart count grows as items are added
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I add the first "<count>" items to the cart
    Then the cart badge should show "<count>"
    And all items should be in the cart when count is "<count>"

    Examples:
      | count |
      | 1     |
      | 2     |
      | 3     |
      | 4     |
      | 5     |
      | 6     |
