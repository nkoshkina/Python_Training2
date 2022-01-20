from model.contact import Contact


def test_modify_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact("10n", "20n", "30n", "0nick", "0Title", "0Comp", "0address",
                                    "+7911111", "+74560089011", "+790011", "+71123456789",
                                    "test@test0.com", "t@t02.com", "t@t03.com", "localhost/",
                                    "30", "March", "1988", "11", "May", "2021",
                                    "2 address", "/test", "here are notes upd"))
    app.session.logout()