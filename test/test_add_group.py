# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_groups_list()
    group0 = Group(name="testgroup", header="testheader", footer="testfooter")
    app.group.create(group0)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_groups_list()
    old_groups.append(group0)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_groups_list()
    group0 = Group(name="", header="", footer="")
    app.group.create(group0)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_groups_list()
    old_groups.append(group0)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




