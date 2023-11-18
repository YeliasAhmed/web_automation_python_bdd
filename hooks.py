from selenium import webdriver
from page_objects.home_page import HomePage


def before_scenario(context, scenario):

    context.driver = webdriver.Chrome()
    context.home_page = HomePage(context.driver)
    context.home_page.open_google()


def after_scenario(context, scenario):

    if hasattr(context, 'driver'):
        context.driver.quit()
