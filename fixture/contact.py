from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_new(self, contact):
        wd = self.app.wd
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_all_fields(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_all_fields(self, contact):
        wd = self.app.wd
        self.fill_text_field("firstname", contact.firstname)
        self.fill_text_field("middlename", contact.middlename)
        self.fill_text_field("lastname", contact.lastname)
        self.fill_text_field("nickname", contact.nickname)
        self.fill_text_field("title", contact.title)
        self.fill_text_field("company", contact.company)
        self.fill_text_field("address", contact.address)
        self.fill_text_field("home", contact.hphone)
        self.fill_text_field("mobile", contact.mphone)
        self.fill_text_field("work", contact.wphone)
        self.fill_text_field("fax", contact.fax)
        self.fill_text_field("email", contact.email)
        self.fill_text_field("email2", contact.email2)
        self.fill_text_field("email3", contact.email3)
        self.fill_text_field("homepage", contact.homepage)
        self.selected_field("bday", contact.dbirthday)
        self.selected_field("bmonth", contact.mbirthday)
        self.fill_text_field("byear", contact.ybirthday)
        self.selected_field("aday", contact.danniversary)
        self.selected_field("amonth", contact.manniversary)
        self.fill_text_field("ayear", contact.yanniversary)
        self.fill_text_field("address2", contact.saddress)
        self.fill_text_field("phone2", contact.shome)
        self.fill_text_field("notes", contact.snotes)

    def fill_text_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def selected_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            Select(wd.find_element_by_name(field)).select_by_visible_text(text)

    def modify_first_contact(self, contact):
        self.modify_contact_by_index(0, contact)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.click_home_link()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        # Fill fields
        self.fill_all_fields(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.click_home_link()
        self.select_contact_by_index(index)
        self.click_delete_button()
        self.alert_accept()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def alert_accept(self):
        wd = self.app.wd
        # Confirm deleting
        wd.switch_to.alert.accept()

    def click_delete_button(self):
        wd = self.app.wd
        # Click Delete button
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def click_home_link(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_xpath("//[@value='Send e-Mail']")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.click_home_link()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.click_home_link()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath("//tbody/tr[@name='entry']"):
                lastname = element.find_element_by_xpath("td[2]").text
                firstname = element.find_element_by_xpath("td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)


