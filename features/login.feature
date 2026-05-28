Feature: Saucedemo login
  Tests login success and failure cases with multiple credentials

  Scenario Outline: Login attempts
    Given I open the login page
    When I login with username "<username>" and password "<password>"
    Then the login should be "<result>"

    Examples:
      | username        | password        | result  |
      | standard_user   | secret_sauce    | success |
      | locked_out_user | secret_sauce    | failure |
      | invalid_user    | wrong_password  | failure |
      | problem_user    | secret_sauce    | success |
