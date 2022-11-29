import pytest
from selenium import webdriver
from Library.config import Config


import time
# path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe"
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager


#CROSS BROWSING
@pytest.fixture(params=["Chrome"])
def _driver(request):
    if request.param=="Chrome":
        driver = webdriver.Chrome(executable_path=Config.Chrome_Driver_Path)
    elif request.param=="Firefox":
        driver=webdriver.Firefox(GeckoDriverManager().install())


    elif request.param=="Edge":
        driver=webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(Config.URL)
    driver.maximize_window()
    driver.implicitly_wait(60)

    yield driver
    print(driver.title)
    path=r'C:\Users\hp\PycharmProjects\Cleartripproject\screenshot\\'
    driver.save_screenshot(path+"test_login.png")
    # driver.close()