from model.contact import Contact


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()