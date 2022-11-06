# -*- coding: utf-8 -*-
from model.project import Project

def test_add_project_soap(app, db, check_ui, json_projects):
    project0 = json_projects
    old_projects = app.soap.get_projects_soap()
    app.project.create(project0)
    new_projects = app.soap.get_projects_soap()
    old_projects.append(Project(project0.id, project0.projectName))
        #Project(project0.id, project0.projectName, project0.description))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)


