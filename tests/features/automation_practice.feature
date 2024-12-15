Feature: Automation Practice
  As a software tester, I want to check all functionality of the automation practice page
  so that I can ensure that the page is working as expected

  Scenario: Check the link is working on the page
    Given User is on Homepage
    When user click on the link
    Then link text should be printed
    And user should be redirected to correct link