
from model.project import Project
import time




class ProjectHelper:
    def __init__(self, app):
        self.app = app

    project_cache = None

    def go_to_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_overview_page.php"):
            wd.find_element_by_link_text("Manage").click()
            time.sleep(1)
            wd.find_element_by_link_text("Manage Projects").click()
            time.sleep(1)

    def create_project(self, project):
        wd = self.app.wd
        self.go_to_project_page()
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        time.sleep(1)
        self.fill_project_form(project)
        time.sleep(1)

        wd.find_element_by_css_selector("input[value='Add Project']").click()
        time.sleep(2)
        self.go_to_project_page()
        self.project_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)
        self.choose_status()
        self.choose_view_status()

    def choose_status(self):
        wd = self.app.wd
        wd.find_element_by_name("status").click()
        wd.find_element_by_css_selector("option[value='30']").click()

    def choose_view_status(self):
        wd = self.app.wd
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_css_selector("option[value='50']").click()

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector("tr.row-1 a, tr.row-2 a"):
                text = element.text
                self.project_cache.append(Project(name=text))
        return list(self.project_cache)

    def count(self):
        wd = self.app.wd
        self.go_to_project_page()
        return len(wd.find_elements_by_css_selector("tr.row-1 a, tr.row-2 a"))


    def delete_project_by_index(self, index):
        wd = self.app.wd
        # self.go_to_project_page()
        self.select_project_by_index(index)
        time.sleep(2)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(2)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        time.sleep(2)
        self.go_to_project_page()
        self.group_cache = None

    def select_project_by_index(self, index):
            wd = self.app.wd
            self.go_to_project_page()
            wd.find_elements_by_css_selector("tr.row-1 a, tr.row-2 a")[index].click()




