# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    assert len(new_groups) == len(old_groups) - 1
    old_groups[0:1] = []
    assert new_groups == old_groups





