from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe"

driver=webdriver.Chrome(path)
driver.get("https://www.cleartrip.com/activate/iIi7ejtTr151YFzo")
driver.implicitly_wait(50)
driver.maximize_window()
#email id textfield
driver.find_element_by_id("username1").send_keys("harsithgow123@gmail.com")
#createaccount button
driver.find_element_by_xpath('//button[@id="registerButton"]').click()
#password textfield
driver.find_element_by_xpath('//input[@name="password"]').send_keys("Harshithagowda@12")
#dropdown
titles=driver.find_elements("xpath","//select[@name='title']//option")
for title in titles:
    if title.text=="Mrs":
        title.click()
        break
#firstname textfield
driver.find_element("xpath",'//input[@name="first_name"]').send_keys("Harshith")
#lastname textfield
driver.find_element("xpath",'//input[@name="last_name"]').send_keys("Reddy")
#countycode dropdown
number =driver.find_elements("xpath","//select[@id='country_code']//option")
for number in number:
    if number.text=="India(+91)":
        number.click()
        break
# driver.execute_script("window.scrollBy(0,400)","")
#mobile number textfield
driver.find_element("xpath",'//input[@class="mobile span selflabel"]').send_keys(9848012338)
#create button
driver.find_element("xpath","(//button[contains(@type,'submit')])[3]").click()

# driver.refresh()
# driver.find_element_by_id("username1").send_keys("harsithagowda123@gmail.com")
# #createaccount button
# driver.find_element_by_xpath('//button[@id="registerButton"]').click()
# time.sleep(2)
# driver.find_element("xpath","//input[@title='Your account password']").send_keys("Harshithagowda@12")
# driver.find_element("xpath","//button[@id='signInButton']").click()
# time.sleep(2)

#login
# driver.get("https://www.cleartrip.com/")
# driver.find_element_by_xpath('//button[text()="Log in / Sign up"]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//span[text()="Continue with Email"]').click()
# #enter registered emailid
# driver.find_element_by_xpath('//input[@placeholder="Enter registered email address"]').send_keys("shivanigv15@gmail.com")
# #enter password
# driver.find_element_by_xpath('//input[@placeholder="Enter password"]').send_keys("Shivanigv@15")
# time.sleep(2)
# #enter login button
# driver.find_element_by_xpath('//span[@class="fs-3 fw-550"]').click()

