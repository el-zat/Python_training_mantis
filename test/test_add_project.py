# -*- coding: utf-8 -*-
from model.project import Project


def test_test(app):

    old_projects = app.project_helper.get_project_list()
    project = Project(name="New project", description="This is a test project")
    app.project_helper.create_project(project)
    new_projects = app.project_helper.get_project_list()
    assert len(old_projects) + 1 == app.group_helper.count()
    old_projects.append(project)
    # assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project_helper.get_project_list(), key=Project.id_or_max)

