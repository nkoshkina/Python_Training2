# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_sign_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen1, maxlen2):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen1))]) \
            +"@" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen1))]) \
            +"." + "".join([random.choice(symbols) for i in range(2)])

def random_number(prefix, maxlen):
        symbols = string.digits
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [ Contact(firstname="")] + \
        [
       Contact(firstname=random_string("", 8), middlename=random_string("", 10), lastname=random_string("", 15),
            nickname=random_string("", 8),
            title=random_string("", 10), company=random_string("", 15), address=random_sign_string("", 20),
            hphone=random_number("+7",10), mphone=random_number("+",11), wphone=random_number("+7",10),
            fax=random_number("+7",10),
            email=random_email("", 7,5), email2=random_email("", 7,5), email3=random_email("", 7,5),
            homepage=random_string("", 15),
            saddress=random_sign_string("", 20), sphone=random_number("+",11), snotes=random_sign_string("", 30))
    for i in range(2)]

@pytest.mark.parametrize("contact0", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact_full_data(app, contact0):
    old_contacts = app.contact.get_contacts_list()
#    contact0 = Contact("1n", "2n", "3n", "nick", "Title", "Comp", "address",
#                       "+7900000", "+745600890", "+7900", "+723456789",
#                        "test@test.com", "t@t2.com", "t@t3.com", "localhost",
#                        "3", "May", "1998", "13", "April", "2020",
#                        "sec address", "//test", "here are notes")
    app.contact.add_new(contact0)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact0)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
