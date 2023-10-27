# Created by bhavani at 10/14/23
Feature:Test for free subscription in Reelly page
  Scenario: Verify user can click free subcription to view free subcription page
    Given Open the Reelly main page
    When Login to the Reelly page
    #When Wait for 3 sec
    Then Click on settings menu
    #Then Click on Get a free subscription
    Then Switch to the new tab
    Then Verify the Get a month of free subscription! in the new tab
