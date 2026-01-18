Feature: Login functionality
    As a user, I want to log in to access the inventory.

    Scenario: Successful login with valid credentials

        Given I open saucedemo website
        When I log in with valid credentials
        Then I should be redirected to the inventory page