from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact("1n", "2n", "3n", "", "Title", "Comp", "address",
                                    "", "", "+7900", "+723456789",
                                    "test@test.com", "t@t2.com", "t@t3.com", "localhost",
                                    "3", "May", "1998", "13", "April", "2020",
                                    "sec address", "//test", "here are notes"))

    app.contact.modify_first_contact(Contact("10n", "20n", "30n", "0nick", "0Title", "0Comp", "0address",
                                    "+7911111", "+74560089011", "+790011", "+71123456789",
                                    "test@test0.com", "t@t02.com", "t@t03.com", "localhost/",
                                    "30", "March", "1988", "11", "May", "2021",
                                    "2 address", "/test", "here are notes upd"))
