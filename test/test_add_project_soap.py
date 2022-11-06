# -*- coding: utf-8 -*-
from model.project import Project

def test_add_project(app, db, check_ui, json_projects, username, password):
    project0 = json_projects
    #old_projects = app.soap.get_projects_soap(username,password)
    app.project.create(project0)
    #new_projects = app.soap.get_projects_soap(username,password)
    #old_projects.append(Project(project0.id, project0.projectName, project0.description))
    #assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
    #if check_ui:
    #    print("CHECK_UI")
    #    assert sorted(new_projects, key=Project.id_or_max) == \
    #           sorted(app.projects.get_projects_list(), key=Project.id_or_max)


