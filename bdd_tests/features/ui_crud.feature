Feature: UI
  Allows to manage users and groups (but slower)

  Background:
    Given I opened the site
    And I entered the admin's credentials
    And I have logged in
    And I opened the Users page

  Scenario: Reading a user
    When I enter 'admin' into the search bar
    And I press the Search button

    Then The result entry is the user's name
    And I log out of the site