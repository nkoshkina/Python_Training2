# -*- coding: utf-8 -*-
import allure

from model.group import Group

def test_add_group(app, db, check_ui, json_groups):
    group0 = json_groups
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with allure.step("When i add group %s to the list" % group0):
        app.group.create(group0)
    with allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group0)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            print("CHECK_UI")
            assert sorted(new_groups, key=Group.id_or_max) == \
                   sorted(app.group.get_groups_list(), key=Group.id_or_max)


