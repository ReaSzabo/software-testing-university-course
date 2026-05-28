Feature: Cart remove button count growth
  Tests that remove button count grows with items added to cart

  Scenario Outline: Remove buttons grow with cart items
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I add the first "<count>" items to the cart
    And I open the cart
    Then the cart should have "<count>" items
    And the cart should show "<count>" remove buttons
    And all items should be in the cart when remove count is "<count>"

    Examples:
      | count |
      | 1     |
      | 2     |
      | 3     |
      | 4     |
      | 5     |
      | 6     |
