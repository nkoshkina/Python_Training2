from model.contact import Contact
from random import randrange


def test_modify_some_contact_all_data(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n",
                                    snotes="here are notes"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact0 = json_contacts
    contact0.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact0)
    assert app.contact.count() == len(old_contacts)
    new_contacts = app.contact.get_contacts_list()
    old_contacts[index] = contact0
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

