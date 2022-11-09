Feature: Арі
  Allows to manage users and groups

  Scenario Outline: Creating a user
    Given I am the admin
    And I have the endpoint
    When User has name '<name>' and email '<email>'
    And I send a POST request
    Then I should get the '<code>' code
    And The '<schema>' schema is correct
    And I receive the user's URL
    Examples:
      | name     | email             | code | schema         |
      | yvchenko | yvchenko@test.com | 201  | user           |
      | yvchenko | yvchenko@test.com | 400  | username_error |
      |          |                   | 400  | username_error |


  Scenario Outline: Reading the user
    Given I am the admin
    And I have created a user
    When User has name '<name>' and email '<email>'
    And I send a GET request
    Then I should get the '<code>' code
    And The '<schema>' schema is correct
    And The credentials match the payload
    Examples:
      | name     | email             | code | schema |
      | yvchenko | yvchenko@test.com | 200  | user   |

  Scenario Outline: Changing the user's email
    Given I am the admin
    And I have created a user
    When User has name '<name>' and email '<email>'
    And I send a PUT request
    Then I should get the '<code>' code
    And The '<schema>' schema is correct
    And The credentials match the payload
    Examples:
      | name     | email                  | code | schema |
      | yvchenko | yvchenko@test.com      | 200  | user   |
      | yvchenko |                        | 200  | user   |
      | yvchenko | another_email@mail.net | 200  | user   |

  Scenario Outline: Changing the user's group
    Given I am the admin
    And I have created a user
    When I create a new group
    And User has name '<name>' and email '<email>'
    And I add the group to the payload
    And I send a PUT request
    Then I should get the '<code>' code
    And The '<schema>' schema is correct
    And The group was added
    Then I delete the group
    Examples:
      | name     | email              | code | schema |
      | yvchenko | new_email@test.com | 200  | user   |

  Scenario: Deleting the user
    Given I am the admin
    And I have created a user
    When I send a DELETE request
    Then I should get the '204' code

  Scenario: Trying to find a deleted user
    Given I am the admin
    And I have created a user
    When I send a GET request
    Then I should get the '404' code
    And The 'not_found' schema is correct
    And The message says Not found