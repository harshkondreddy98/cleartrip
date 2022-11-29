import pytest
from POM.Login import Loginpage
from data import reading_objects
from Library.config import Config

class TestLoginPage:
    details = reading_objects.read_data()
    @pytest.mark.parametrize("mail_id,password,firstname,lastname,mobileno",details)
    def test_login(self,mail_id,password,firstname,lastname,mobileno,_driver):
        lp = Loginpage(_driver)
        lp.mailid(mail_id)
        lp.createaccount()
        lp.password(password)
        lp.select_title()
        lp.firstname(firstname)
        lp.lastname(lastname)
        lp.countrycode()
        lp.mobileno(int(mobileno))
        lp.create()