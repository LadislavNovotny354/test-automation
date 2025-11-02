from selenium.webdriver.common.by import By

class HomePage:
    URL = "https://www.investown.cz"
    START_BUTTON = (By.XPATH, "//a[contains(.,'Začít investovat') or contains(.,'Začít')]")
    NAV_OFFER = (By.LINK_TEXT, "Nabídka investic")
    LOGIN_LINK = (By.LINK_TEXT, "Přihlásit se")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def click_start(self):
        self.driver.find_element(*self.START_BUTTON).click()

    def go_to_offers(self):
        self.driver.find_element(*self.NAV_OFFER).click()

    def open_login(self):
        self.driver.find_element(*self.LOGIN_LINK).click()
