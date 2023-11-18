import time

from behave import *
from selenium import webdriver
from page_objects.home_page import HomePage


@given(u'user on the google home page')
def step_given_user_on_google_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.home_page = HomePage(context.driver)
    context.home_page.open_google()


@when(u'the user searches for {search_term}')
def step_when_user_searches(context, search_term):
    context.home_page.search_for(search_term)


@then(u'the search results page should be displayed')
def step_then_search_results_page_displayed(context):
    time.sleep(2)
    assert "Dhaka" in context.driver.title

    context.driver.quit()
