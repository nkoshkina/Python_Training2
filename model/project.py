from sys import maxsize

class Project:
    def __init__(self, projectName=None, status=None, igs=None, viewStatus=None,
                 description=None, id=None
                 ):
        self.projectName = projectName
        self.status = status
        self.igs = igs
        self.viewStatus = viewStatus
        self.description = description
        self.id = id

    def __repr__(self):
        # return "%s:%s:%s:%s:%s:%s" % (self.id, self.projectName, self.status, self.igs, self.viewStatus, self.description)
        return "%s:%s" % (self.id, self.projectName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
        (self.projectName == other.projectName or self.projectName is None  or other.projectName is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize