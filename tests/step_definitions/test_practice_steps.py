import time

from pytest_bdd import given, when, then, scenario

from pages_app import home_page

homepage = home_page.HomePage()
alert_box_locator = "//button[contains(text(), 'Generate Alert Box')]"

@scenario(r'../features/automation_practice.feature', 'Check the link is working on the page')
def test_scenario(logger):
    pass


@given('User is on Homepage')
def i_am_on_the_practice_page(logger):
    homepage.navigate_to_home_page()
    logger.info("This is an info message.")




@when('user click on the link')
def i_click_on_the_link(logger):
    homepage.click_on_element(alert_box_locator)
    time.sleep(2)
    homepage.tear_down()
    logger.warning("This is a warning message.")



@then('link text should be printed')
def i_should_be_redirected_to_the_correct_page(logger):
    logger.debug("This is a debug message.")
    pass


@then('user should be redirected to correct link')
def i_should_see_the_correct_page_title(logger):
    logger.warning("This is a warning message.")
    pass
