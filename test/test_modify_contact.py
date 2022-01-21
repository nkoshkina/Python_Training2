from model.contact import Contact
from random import randrange


def test_modify_some_contact_all_data(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n",
                                    snotes="here are notes"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact0 = Contact("10n", "20n", "30n", "0nick", "0Title", "0Comp", "0address",
                        "+7911111", "+74560089011", "+790011", "+71123456789",
                        "test@test0.com", "t@t02.com", "t@t03.com", "localhost/",
                         "30", "March", "1988", "11", "May", "2021",
                        "2 address", "/test", "here are notes upd")
    contact0.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact0)
    assert app.contact.count() == len(old_contacts)
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact0
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_some_contact_some_fields(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n",
                                    snotes="here are notes"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact0 = Contact(snotes="here are new notes")
    contact0.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact0)
    assert app.contact.count() == len(old_contacts)
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact0
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

