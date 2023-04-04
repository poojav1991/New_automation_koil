from selenium.webdriver.common.by import By


class deleteuserpage:
    def __init__(self, driver):
        self.driver = driver
        # print("1.1")

    # product = (By.XPATH, "//li[@class='nav-item']/a/p[contains(text(), 'Products')]")
    deletebutton = (By.XPATH, "//div[@class='delete-breadcrumb']")
    succeesmessage = (By.XPATH, "//div[@class='alert alert-success']")
    yesdelete = (By.XPATH, "//button[contains(.,'Yes, delete it!')]")
    checkboxes = (By.XPATH, "//tr/th/input[@id='flexCheckDefault']")

    def get_checkboxes(self):
        return self.driver.find_elements(*deleteuserpage.checkboxes)
    def get_deletebutton(self):
        return self.driver.find_element(*deleteuserpage.deletebutton)
    def get_succeesmessage(self):
        return self.driver.find_element(*deleteuserpage.succeesmessage)
    def get_yesdelete(self):
        return self.driver.find_element(*deleteuserpage.yesdelete)
