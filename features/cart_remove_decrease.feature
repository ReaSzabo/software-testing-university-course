Feature: Cart remove button decreases item count
  Tests that removing items one-by-one decreases cart item count to zero

  Scenario Outline: Cart count decreases as items are removed
    Given I open the login page
    When I login with username "standard_user" and password "secret_sauce"
    And I add all items to the cart
    And I open the cart
    And I remove "<removed>" items from the cart
    Then the cart should have "<remaining>" items remaining

    Examples:
      | removed | remaining |
      | 1       | 5         |
      | 2       | 4         |
      | 3       | 3         |
      | 4       | 2         |
      | 5       | 1         |
      | 6       | 0         |
