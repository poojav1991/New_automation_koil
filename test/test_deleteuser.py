from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import pytest
from selenium.webdriver.support.select import Select

from testdata.deleteuserdata import deleteuserdata

"""
from PythonSelfFramework.pageobjects.listpage import listpage
from PythonSelfFramework.pageobjects.loginpage import loginpage
from PythonSelfFramework.testdata.adduserdata import adduserdata
from PythonSelfFramework.utilities.BaseClass import BaseClass

"""
from pageobjects.addpage import addpage
from pageobjects.listpage import listpage
from pageobjects.loginpage import loginpage
from testdata.adduserdata import adduserdata
from utilities.BaseClass import BaseClass


class TestDeleteUser(BaseClass):
    def test_login(self):
        log = self.getlogger()
        login_credential = self.login_credential()
        LoginPage = loginpage(self.driver)  # This one is return from login page object
        log.info("Login with this mobile number " + login_credential["mobileno"])
        log.info("Login with this password " + login_credential["password"])
        LoginPage.get_mobileno().send_keys(login_credential["mobileno"])  # this one is sent keyword to input box
        LoginPage.get_password().send_keys(login_credential["password"])  # this one is sent keyword to input box
        self.Login().click()

    def test_deleteUser(self):
        log = self.getlogger()
        ListPage = listpage(self.driver)  # This one is return from Lostpage.py object adduser = ListPage.UserList()
        deleteuser = ListPage.UserdeleteList()
        # adduser.ProductAdd().click()
        # print(getdata["userid"])
        #print("ddsfsdfsdf")
        checkbox = deleteuser.get_checkboxes()
        time.sleep(3)
        #print("458")
        for checks in checkbox:
            #print("123")
            print(checks.get_attribute("value"))
            checks.click()
            time.sleep(2)
        deleteuser.get_deletebutton().click()
        #time.sleep(2)
        deleteuser.get_yesdelete().click()
        time.sleep(2)
        # if getdata != None:
        #success_text = deleteuser.get_succeesmessage().text
        #if success_text != "":
         #   log.info("success message recieved from add user " + success_text)
        #time.sleep(5)
        # assert ("Successfully" in success_text)
        #time.sleep(5)

    # @pytest.fixture(params=[("9876514710","Psdds0rd"),
    #                       ("9876788788","P@ssw0rd"),
    #                       ("9876788788","P@sdsdsdsdsd"),
    #                       ("9876543210","P@ssw0rd")]) This fixture using tupple data
    # @pytest.fixture(params=deleteuserdata.test_deleteuserdata)  # This fixture using dictionary data with key and value
    # def getdata(self, request):
    # return request.param
