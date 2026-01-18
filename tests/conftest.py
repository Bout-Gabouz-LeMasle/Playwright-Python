import os
import pytest
from playwright.sync_api import Page
from pages.home.home_page import HomePage
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def user_data():
    return {
        "username": os.getenv("TEST_USERNAME"),
        "password": os.getenv("TEST_PASSWORD")
    }

@pytest.fixture
def home(page: Page, base_url: str):
    return HomePage(page, base_url)