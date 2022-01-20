from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("1n", "2n", "3n", "", "Title", "Comp", "address",
                                    "", "", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May", "1998", "13", "April", "2020",
                                    "sec address", "//test", "here are notes"))
    app.contact.delete_first_contact()
