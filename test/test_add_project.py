# -*- coding: utf-8 -*-
from model.project import Project
from data.project_testdata import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login("administrator", "root")
    old_projects = app.soap.get_projects_list_administrator()
    print(len(old_projects))
    app.project_helper.create_project(project)
    new_projects = app.soap.get_projects_list_administrator()
    assert len(old_projects) + 1 == len(new_projects)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.soap.get_projects_list_administrator(),
                                                                 key=Project.id_or_max)
