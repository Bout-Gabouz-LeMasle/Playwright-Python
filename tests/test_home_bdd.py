from pytest_bdd import scenario, given, when, then, parsers
from playwright.sync_api import expect
import re

@scenario('../features/login.feature', 'Successful login with valid credentials')
def test_home_bdd():
    pass

@given("I open saucedemo website")
def i_am_on_the_home_page(home):
    home.navigate()

@when("I log in with valid credentials")
def i_log_in_valid(home, user_data):
    home.login(user_data["username"], user_data["password"])

@then("I should be redirected to the inventory page")
def i_should_be_redirected(home):
    expect(home.page).to_have_url(re.compile("inventory.html"))