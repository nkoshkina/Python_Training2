class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill new group form
        self.fill_all_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.click_return_to_groups_page_link()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        self.click_edit_button()
        self.fill_all_fields(group)
        # click update group
        wd.find_element_by_name("update").click()
        self.click_return_to_groups_page_link()

    def fill_all_fields(self, group):
        wd = self.app.wd
        # fill new group form
        self.fill_field("group_name", group.name)
        self.fill_field("group_header", group.header)
        self.fill_field("group_footer", group.footer)

    def fill_field(self, field, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def click_edit_button(self):
        wd = self.app.wd
        # click Edit group
        wd.find_element_by_name("edit").click()

    def select_first_group(self):
        wd = self.app.wd
        # select 1st group
        wd.find_element_by_name("selected[]").click()

    def open_groups(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) >0:
            return
        wd.find_element_by_link_text("groups").click()

    def click_return_to_groups_page_link(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        # select 1st group
        self.select_first_group()
        # click Delete
        self.click_delete_button()
        self.click_return_to_groups_page_link()

    def click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements_by_name("selected[]"))

