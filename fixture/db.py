import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host="127.0.0.1", database="addressbook",
                            user="root", password="", autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_footer,"
                       "group_header from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()