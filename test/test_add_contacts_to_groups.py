from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test group"))
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact("1n", "2n", "3n", "", "Title", "Comp", "address",
                                    "", "", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May", "1998", "13", "April", "2020",
                                    "sec address", "//test", "here are notes"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact0 = random.choice(old_contacts)
    group0 = random.choice(old_groups)
    old_list = db.get_contacts_in_group(group0.id)
    app.contact.add_contact_to_group_by_id(contact0.id, group0.name)
    new_list = db.get_contacts_in_group(group0.id)
    old_list.append(contact0)
    assert new_list == old_list

