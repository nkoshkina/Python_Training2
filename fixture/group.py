class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill new group form
        self.fill_all_fields(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        self.click_edit_button()
        self.fill_all_fields(group)
        # click update group
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def fill_all_fields(self, group):
        wd = self.app.wd
        # fill new group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

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
        wd.find_element_by_link_text("groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        # select 1st group
        self.select_first_group()
        # click Delete
        self.click_delete_button()
        self.return_to_groups_page()

    def click_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()


