import this

import self as self
from selenium.webdriver.common.by import By


class editpage:
    def __init__(self, driver):
        self.driver = driver
        #self.userid = userid
        # print("1.1")
        #print(userid)
        #user = self.userid
        #global self.userid

    # product = (By.XPATH, "//li[@class='nav-item']/a/p[contains(text(), 'Products')]")
    #editpath = "//tr/td[@class='table-action']/span/a[@title='Edit'][contains(@href,'" + str(userid) + "')]"
    #edit = (By.XPATH, "//tr[position()=2]/td[@class='table-action']/span/a[@title='Edit']")
    #edit = (By.XPATH, "//tr/td[@class='table-action']/span/a[@title='Edit'][contains(@href,'" + str(self.userid) + "')]")
    #editid = 0
    #print("sdfsdfsdfsdffsdf")
    #print(self.userid)
    firmname = (By.XPATH, "//*[@id='firmname']")
    ownername = (By.ID, "ownername")
    mobileno = (By.ID, "mobileno")
    genp = (By.ID, "genp")
    setting_search_add = (By.ID, "setting-search-add")
    searchAddressChecked = (By.ID, "searchAddressChecked")
    city = (By.ID, "city")
    status = (By.XPATH, "//select[@name='status']")
    submituser = (By.CSS_SELECTOR, "[type='submit']")
    succeesmessage = (By.XPATH, "//div[@class='alert alert-success']")
    # genp = (By.ID, "genp")
    checkboxes = (By.XPATH, "//label[@class='form-check-label']")

    def Productcheckboxes(self):
        return self.driver.find_elements(*editpage.checkboxes)
    def get_status(self):
        return self.driver.find_element(*editpage.status)
    def User_Edit(self,userid):
        #print(userid)
        editpath = "//tr/td[@class='table-action']/span/a[@title='Edit'][contains(@href,'" + str(userid) + "')]"
        #print(editpath)
        #edit = str((By.XPATH, "//tr/td[@class='table-action']/span/a[@title='Edit'][contains(@href,'" + str(editid) + "')]"))
        #print(self.driver.find_element(By.XPATH, editpath))
        return self.driver.find_element(By.XPATH, editpath)

    def get_firmname(self):
        # print("test get firmname")
        return self.driver.find_element(*editpage.firmname)

    def get_ownername(self):
        return self.driver.find_element(*editpage.ownername)

    def get_mobileno(self):
        return self.driver.find_element(*editpage.mobileno)

    def get_genp(self):
        return self.driver.find_element(*editpage.genp)

    def get_setting_search_add(self):
        return self.driver.find_element(*editpage.setting_search_add)

    def get_searchAddressChecked(self):
        return self.driver.find_element(*editpage.searchAddressChecked)

    def get_city(self):
        return self.driver.find_element(*editpage.city)

    def get_submituser(self):
        return self.driver.find_element(*editpage.submituser)

    def get_succeesmessage(self):
        return self.driver.find_element(*editpage.succeesmessage)