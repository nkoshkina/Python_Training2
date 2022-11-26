# -*- coding: utf-8 -*-
import allure
from model.contact import Contact

def test_add_new_contact_full_data(app, db, check_ui, json_contacts):
    contact0 = json_contacts
    with allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with allure.step("When i add contact %s to the list" % contact0):
        app.contact.add_new(contact0)
    with allure.step('Then the new contact list is equal to the old list with the added contact'):
        new_contacts = db.get_contact_list()
        old_contacts.append(contact0)
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == \
                   sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
