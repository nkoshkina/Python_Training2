from model.group import Group
from random import randrange


def test_modify_some_group_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test group"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group0 = Group(name="test1", header="test1", footer="test1")
    group0.id = old_groups[index].id
    app.group.modify_group_by_index(index, group0)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[index] = group0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group0 = Group(header="updated header")
    group0.id = old_groups[index].id
    app.group.modify_group_by_index(index, group0)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[index] = group0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_some_group_name_and_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    group0 = Group(name="upd name", footer="upd footer")
    group0.id = old_groups[index].id
    app.group.modify_group_by_index(index, group0)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[index] = group0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
