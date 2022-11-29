Feature: Signup/login
  Scenario Outline: User should be able to Signup and login into the application
    Given Open the chrome browser enter the valid URL
    When enter the email_id "<email_id>"
    And click on create account button
    And enter the password "<password>"
    And click the title
    And enter the first name "<firstname>"
    And enter the last name "<lastname>"
    And click on country code
    And enter the mobile no "<mobile_no>"
    And click on create account
    Then cleartrip home page should open
#    And close the browser
    Examples:
    |email_id|password|firstname|lastname|mobile_no|
    |VarunReddy1234@gmail.com|Varun@ygut1|Varun|At|9765478234|