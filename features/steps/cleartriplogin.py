import re
import time
from behave import *
from selenium import webdriver

@given(u'Open the chrome browser enter the valid URL')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")
    context.driver.get("https://www.cleartrip.com/activate/iIi7ejtTr151YFzo")
    context.driver.implicitly_wait(30)
#

@when(u'enter the email_id "{email_id}"')
def step_impl(context,email_id):
    pattern = r"\w+@gmail\.com"
    result = re.findall(pattern, email_id)
    assert result, "invalid email_id"
    context.driver.find_element("id","username1").send_keys(email_id)


@when(u'click on create account button')
def step_impl(context):
    context.driver.find_element("xpath",'//button[@id="registerButton"]').click()
    time.sleep(2)


@when(u'enter the password "{password}"')
def step_impl(context,password):
    context.driver.find_element("xpath",'//input[@name="password"]').send_keys(password)


@when(u'click the title')
def step_impl(context):
    titles = context.driver.find_elements("xpath", "//select[@name='title']//option")
    for title in titles:
        if title.text == "Mrs":
            title.click()
            break


@when(u'enter the first name "{firstname}"')
def step_impl(context,firstname):
    context.driver.find_element("xpath", '//input[@name="first_name"]').send_keys(firstname)


@when(u'enter the last name "{lastname}"')
def step_impl(context,lastname):
    context.driver.find_element("xpath",'//input[@name="last_name"]').send_keys(lastname)


@when(u'click on country code')
def step_impl(context):
    number = context.driver.find_elements("xpath", "//select[@id='country_code']//option")
    for number in number:
        if number.text == "India(+91)":
            number.click()
            break


@when(u'enter the mobile no "{mobile_no}"')
def step_impl(context,mobile_no):
    context.driver.find_element("xpath", '//input[@class="mobile span selflabel"]').send_keys(mobile_no)


@when(u'click on create account')
def step_impl(context):
    context.driver.find_element("xpath", "(//button[contains(@type,'submit')])[3]").click()
    time.sleep(2)

@then(u'cleartrip home page should open')
def step_impl(context):
    assert True
    time.sleep(60)

# @then(u'close the browser')
# def step_impl(context):
#     context.driver.close()


