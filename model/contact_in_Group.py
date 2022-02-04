from sys import maxsize

class ContactInGroup:
    def __init__(self, firstname=None, lastname=None,
                 id=None, group_id=None, group_name=None
                 ):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.group_id = group_id
        self.group_name = group_name


    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.group_id, self.group_name)

