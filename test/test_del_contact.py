from model.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("1n", "2n", "3n", "", "Title", "Comp", "address",
                                    "", "", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May", "1998", "13", "April", "2020",
                                    "sec address", "//test", "here are notes"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert app.contact.count() == len(old_contacts) - 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts
