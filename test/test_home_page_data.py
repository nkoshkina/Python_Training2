from model.contact import Contact
import re
from random import randrange

def test_data_on_home_and_edit_pages(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n", address="Test address",
                                    hphone="+09875444", mphone="+79897896756", fax="+70008986756",
                                    email="t@test.com", email2="test2@t.com", email3="test@test3.com",
                                    snotes="here are notes"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_home_page(contact_from_edit_page)

def clear_phones(s):
    return re.sub("[()/ -]", "", s)


def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",
        map(lambda x: clear_phones(x), filter(lambda x: x is not None,
            [contact.hphone, contact.mphone, contact.wphone, contact.sphone]))))

def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x!= "",
        map(lambda x: x, filter(lambda x: x is not None,
            [contact.email, contact.email2, contact.email3]))))
