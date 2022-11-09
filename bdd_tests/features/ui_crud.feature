@bdd @ui
Feature: UI
  Allows to manage users and groups (but slower)

  Background:
    Given I opened the site
    And I entered the admin's credentials
    And I have logged in

  Scenario: Creating a new user
    When I press the Create button
    And I fill in the username field with 'yvchenko'
    And I fill in the password field
    And I fill in the confirm password field
    And I press the Save button


    Then A user 'yvchenko' is created
    And I log out of the site

  Scenario Outline: Finding a user by name
    Given I opened the Users page
    And I enter '<username>' into the search bar
    And I press the Search button

    Then The result entry is the '<username>' name

    And I log out of the site

    Examples:
      | username |
      | yvchenko |
      | admin    |

  Scenario: Checking filters
    Given I opened the Users page

    When I click on Superuser filter

    Then The result entries do not contain 'admin'

    And I log out of the site

  Scenario: Updating user's info
    Given I opened the Users page
    And I enter 'yvchenko' into the search bar
    And I press the Search button
    And I click on the result entry

    When I fill in the Name field with 'nat'
    And I fill in the Last name field with 'yuvchenko'
    And I fill in the Email field with 'nat@example.com'
    And I press the Continue button

    Then I receive a notification that user 'yvchenko' is changed

    And I log out of the site

  Scenario: Checking the updated user's info
    Given I opened the Users page
    And I enter 'yvchenko' into the search bar
    And I press the Search button
    And I click on the result entry

    Then The Name is 'nat'
    And The Last name is 'yuvchenko'
    And The Email is 'nat@example.com'

    And I log out of the site

  Scenario: Deleting a user
    Given I opened the Users page
    And I enter 'yvchenko' into the search bar
    And I press the Search button
    And I click on the result entry

    When I press the Delete button
    And I press the Submit button

    Then I receive a notification that user 'yvchenko' is deleted
    And I can't find 'yvchenko' in the list of users

    And I log out of the site