from selenium.webdriver.common.by import By

from pageobjects.addpage import addpage
from pageobjects.editpage import editpage



class listpage:
    def __init__(self, driver):
        self.driver = driver
        #print("1.1")

    product = (By.XPATH, "//li[@class='nav-item']/a/p[contains(text(), 'Products')]")
    user = (By.XPATH, "(//li[@class='nav-item']/a/p[contains(text(), 'Users')])[1]")
    #useredit =(By.XPATH,"//tr[position()=1]/td[@class='table-action']/span/a[@title='Edit']")
    def UserList(self):
        #print("1.487878")
        self.driver.find_element(*listpage.user).click()
        AddPage = addpage(self.driver)
        return AddPage
    def ProductList(self):
        #print("1.487878")
        self.driver.find_element(*listpage.product).click()
        AddPage = addpage(self.driver)
        return AddPage
    def UserEdit(self):
        #print(userid)
        self.driver.find_element(*listpage.user).click()

        EditPage = editpage(self.driver)
        return EditPage

