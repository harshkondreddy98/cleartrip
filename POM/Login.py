from selenium import webdriver
from data import reading_objects
from Library.config import Config
import time
from data import reading_objects

# path=r"C:\Users\hp\Documents\cleartriplogin\createaccount.xlsx"
#
# driver=webdriver.Chrome(executable_path=path)
# driver.get("https://www.cleartrip.com/activate/iIi7ejtTr151YFzo")
# driver.maximize_window()
# driver.implicitly_wait(30)

login_obj= reading_objects.read_locators()
print(login_obj)

class Loginpage:
    def __init__(self,driver):
        self.driver=driver

    def mailid(self,mail_id):
        self.driver.find_element(*login_obj["text_mailid"]).send_keys(mail_id)

    def createaccount(self):
        self.driver.find_element(*login_obj["click_createaccount"]).click()

    def password(self,password):
        self.driver.find_element(*login_obj["text_password"]).send_keys(password)
        time.sleep(2)

    def select_title(self):
        titles = self.driver.find_elements(*login_obj["select_title"])
        for title in titles:
            if title.text == "Ms":
                title.click()
                break

    def firstname(self,firstname):
        self.driver.find_element(*login_obj["text_firstname"]).send_keys(firstname)

    def lastname(self,lastname):
        self.driver.find_element(*login_obj["test_lastname"]).send_keys(lastname)

    def countrycode(self):
        number = self.driver.find_elements(*login_obj["select_countrycode"])
        for number in number:
            if number.text == "India(+91)":
                number.click()
                break

    def mobileno(self,mobileno):
        self.driver.find_element(*login_obj["text_mobileno"]).send_keys(mobileno)
        time.sleep(3)

    def create(self):
        time.sleep(2)
        self.driver.find_element('xpath','//dd[@class="submit"]//button').click()
        time.sleep(20)

# lp=Loginpage()
# lp.mailid()
# lp.createaccount()
# lp.password()
# lp.select_title()
# lp.firstname()
# lp.lastname()
# lp.countrycode()
# lp.mobileno()
# lp.create()