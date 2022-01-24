# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="", footer="")] + \
           [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20)) \
    for i in range(5)
]

@pytest.mark.parametrize("group0", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group0):
    old_groups = app.group.get_groups_list()
    #group0 = Group(name="testgroup", header="testheader", footer="testfooter")
    app.group.create(group0)
    assert app.group.count() == len(old_groups) + 1
    new_groups = app.group.get_groups_list()
    old_groups.append(group0)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



