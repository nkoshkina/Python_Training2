from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.navigation import NavigationHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        #self.navigation = NavigationHelper(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_home_link(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()


    def destroy(self):
        self.wd.quit()
