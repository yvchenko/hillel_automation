Feature: CRUD
  Basic scenarios of creating, reading, updating and deleting a new user

  Scenario: Creating a user
      Given I am the admin
      And I have the endpoint

      When User has name 'yvchenko' and email 'yvchenko@test.com'
      And I send a POST request

      Then I should get the '201' code
      And The 'user' schema is correct
      And I receive the user's URL

  Scenario: Reading the user
      Given I am the admin
      And I have created a user

      When User has name 'yvchenko' and email 'yvchenko@test.com'
      And I send a GET request

      Then I should get the '200' code
      And The 'user' schema is correct
      And The credentials match the payload

  Scenario: Changing the user's email
      Given I am the admin
      And I have created a user

      When User has name 'yvchenko' and email 'new_email@test.com'
      And I send a PUT request

      Then I should get the '200' code
      And The 'user' schema is correct
      And The credentials match the payload

  Scenario: Changing the user's group
      Given I am the admin
      And I have created a user

      When I create a new group
      And User has name 'yvchenko' and email 'new_email@test.com'
      And I add the group to the payload
      And I send a PUT request

      Then I should get the '200' code
      And The 'user' schema is correct
      And The group was added
      Then I delete the group

  Scenario: Deleting the user
      Given I am the admin
      And I have created a user

      When I send a DELETE request

      Then I should get the '204' code