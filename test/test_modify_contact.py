from model.contact import Contact


def test_modify_first_contact_all_data(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n",
                                    snotes="here are notes"))
    old_contacts = app.contact.get_contacts_list()
    contact0 = Contact("10n", "20n", "30n", "0nick", "0Title", "0Comp", "0address",
                        "+7911111", "+74560089011", "+790011", "+71123456789",
                        "test@test0.com", "t@t02.com", "t@t03.com", "localhost/",
                         "30", "March", "1988", "11", "May", "2021",
                        "2 address", "/test", "here are notes upd")
    contact0.id = old_contacts[0].id
    app.contact.modify_first_contact(contact0)
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[0] = contact0
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_some_fields(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n",
                                    snotes="here are notes"))
    old_contacts = app.contact.get_contacts_list()
    contact0 = Contact(snotes="here are new notes")
    contact0.id = old_contacts[0].id
    app.contact.modify_first_contact(contact0)
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contacts)
    old_contacts[0] = contact0
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

