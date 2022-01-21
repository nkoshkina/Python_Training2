# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact_full_data(app):
    old_contacts = app.contact.get_contacts_list()
    contact0 = Contact("1n", "2n", "3n", "nick", "Title", "Comp", "address",
                        "+7900000", "+745600890", "+7900", "+723456789",
                        "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                        "3", "May", "1998", "13", "April", "2020",
                        "sec address", "//test", "here are notes")
    app.contact.add_new(contact0)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact0)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_new_contact_partly_data(app):
    old_contacts = app.contact.get_contacts_list()
    contact0 = Contact(firstname="1n", middlename="2n", lastname="3n",
                       snotes="here are notes")
    app.contact.add_new(contact0)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact0)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
