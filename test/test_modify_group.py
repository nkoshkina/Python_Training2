from model.group import Group


def test_modify_first_group_all_fields(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "test group"))
    old_groups = app.group.get_groups_list()
    group0 = Group(name="test1", header="test1", footer="test1")
    group0.id = old_groups[0].id
    app.group.modify_first_group(group0)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[0] = group0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    old_groups = app.group.get_groups_list()
    group0 = Group(header="updated header")
    group0.id = old_groups[0].id
    app.group.modify_first_group(group0)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[0] = group0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_name_and_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test group"))
    old_groups = app.group.get_groups_list()
    group0 = Group(name="upd name", footer="upd footer")
    group0.id = old_groups[0].id
    app.group.modify_first_group(group0)
    assert app.group.count() == len(old_groups)
    new_groups = app.group.get_groups_list()
    old_groups[0] = group0
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
