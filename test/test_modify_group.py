from model.group import Group

def test_modify_first_group_all_fields(app):
    app.group.modify_first_group(Group(name="test1", header="test1", footer="test1"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="updated header"))



def test_modify_first_group_name_and_footer(app):
    app.group.modify_first_group(Group(name="upd name", footer="upd footer"))
