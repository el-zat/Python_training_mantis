from model.project import Project
from random import randrange


# def test_delete_some_project(app):
#     app.session.login("administrator", "root")
#     if app.project_helper.count() == 0:
#         app.project_helper.create_project(Project(name="Testproject"))
#     old_projects = app.project_helper.get_project_list()
#     index = randrange(len(old_projects))
#     app.project_helper.delete_project_by_index(index)
#     assert len(old_projects) - 1 == app.project_helper.count()
#     print(app.project_helper.count())
#     new_projects = app.project_helper.get_project_list()
#     old_projects[index:index+1] = []
#     assert sorted(new_projects, key=Project.id_or_max) == sorted(app.project_helper.get_project_list(),
#                                                                  key=Project.id_or_max)

def test_delete_some_project(app):
    app.session.login("administrator", "root")
    if app.project_helper.count() == 0:
        app.project_helper.create_project(Project(name="Testproject"))
    old_projects = app.soap.get_projects_list_administrator()
    index = randrange(len(old_projects))
    app.project_helper.delete_project_by_index(index)
    assert len(old_projects) - 1 == app.project_helper.count()
    print(app.project_helper.count())
    new_projects = app.soap.get_projects_list_administrator()
    old_projects[index:index+1] = []
    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.soap.get_projects_list_administrator(),
                                                                 key=Project.id_or_max)