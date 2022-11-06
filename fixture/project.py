from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def open_new_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def create(self, project):
        wd = self.app.wd
        self.open_projects()
        self.open_new_project()
        self.fill_all_fields(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_all_fields(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.projectName)
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        if project.igs == "0":
            # wd.find_element_by_id("inherit-global").get_attribute('checked')
            wd.find_element_by_name("inherit_global").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.viewStatus)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)


    def select_first_project(self):
        wd = self.app.wd
        # select 1st group
        wd.find_element_by_xpath("/html/body/table[3]/tbody/tr[3]/td[1]/a").click()

    def delete_first_project(self):
        wd = self.app.wd
        self.open_projects()
        # select 1st group
        self.select_first_project()
        # click Delete
        self.click_delete_project()

    def click_delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects()
        # select 1st group
        self.select_project_by_id(id)
        # click Delete
        self.click_delete_project()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" %id).click()
