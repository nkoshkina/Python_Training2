import pymysql.cursors
from model.group import Group
from model.contact import Contact
from model.contact_in_Group import ContactInGroup

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

    def get_contact_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select addressbook.id, addressbook.firstname, addressbook.lastname \
                        address_in_groups.group_id,  group_list.group_name\
                           from  address_in_groups \
                           INNER JOIN addressbook\
                           ON addressbook.id = address_in_groups.id \
                           INNER JOIN group_list\
                            ON address_in_groups.group_id = group_list.group_id \
                           where addressbook.deprecated = '0000-00-00 00:00:00' \
                           AND address_in_groups.deprecated = '0000-00-00 00:00:00'\
                           AND group_list.deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, group_id, group_name) = row
                list.append(ContactInGroup(id=str(id), firstname=firstname, lastname=lastname, \
                                    group_id=str(group_id), group_name=group_name))
        finally:
            cursor.close()
        return list

    def get_contacts_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select addressbook.id,  addressbook.firstname, addressbook.lastname, \
                         address_in_groups.group_id \
                            from  address_in_groups \
                            INNER JOIN addressbook\
                            ON addressbook.id = address_in_groups.id \
                            where addressbook.deprecated = '0000-00-00 00:00:00' \
                            AND address_in_groups.deprecated = '0000-00-00 00:00:00'\
                            AND address_in_groups.group_id = " + str(group_id))

            for row in cursor:
                (id, firstname, lastname, group_id) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, \
                                    group=group_id))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, address,\
                        email, email2, email3, \
                        mobile, work, phone2, home \
                           from addressbook where deprecated = '0000-00-00 00:00:00'" \
                           )
            for row in cursor:
                (id, firstname, middlename, lastname, address, email, email2, email3, \
                 mobile, work, phone2, home) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname, \
                                    address=address, email=email, email2=email2, email3=email3, home=home, \
                                    mobile=mobile, work=work, phone2=phone2))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()