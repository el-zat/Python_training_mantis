# -*- coding: utf-8 -*-
from model.project import Project
from data.project_testdata import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login("administrator", "root")
    old_projects = app.project_helper.get_project_list()
    print(len(old_projects))
    app.project_helper.create_project(project)
    new_projects = app.project_helper.get_project_list()
    assert len(old_projects) + 1 == app.project_helper.count()
    old_projects.append(project)
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project_helper.get_project_list(),
                                                                 key=Project.id_or_max)

