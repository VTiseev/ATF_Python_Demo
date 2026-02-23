Feature: Login functionality
  As a user of SauceDemo
  I want to log in
  So that I can see the inventory

  Scenario: Successful login with standard user
    Given I open the login page
    When I login as "standard_user" with password "secret_sauce"
    Then I should see the inventory page


  Scenario Outline: Unsuccessful login with wrong credentials
    Given I open the login page
    When I login as "<username>" with password "<password>"
    Then I should see an error message containing "<error_text>"

    Examples:
      | username        | password     | error_text                                |
      | locked_out_user | secret_sauce | Sorry, this user has been locked out      |
      | standard_user   | wrong_pass   | Username and password do not match        |