from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def get_projects_soap(self, username, password):
        client =Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        return client.service.mc_projects_get_user_accessible(username, password)

