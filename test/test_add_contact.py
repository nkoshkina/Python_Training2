# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact_full_data(app):
    app.contact.add_new(Contact("1n", "2n", "3n", "nick", "Title", "Comp", "address",
                                    "+7900000", "+745600890", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May", "1998", "13", "April", "2020",
                                    "sec address", "//test", "here are notes"))


def test_add_new_contact_partly_data(app):
    app.contact.add_new(Contact(firstname="1n", middlename="2n", lastname="3n",
                                snotes="here are notes"))