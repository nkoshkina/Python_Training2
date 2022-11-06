from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def get_projects_soap(self):
        #username = 'administrator'
        #password = 'root'

        client =Client(self.app.base_url + "api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(self.app.username, self.app.password)
        except WebFault:
            return False
        list = []
        for p in projects:
            list.append(Project(id=p["id"], projectName= p["name"]))
        return (list)