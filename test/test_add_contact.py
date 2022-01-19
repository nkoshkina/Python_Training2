# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact("1n", "2n", "3n", "nick", "Title", "Comp", "address",
                                    "+7900000", "+745600890", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May", "1998", "13", "April", "2020",
                                    "sec address", "//test", "here are notes"))
    app.session.logout()

