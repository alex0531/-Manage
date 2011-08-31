#from mail.models import*
import workstatus.mail.models
from models import Project, User

def addMessage(emailAddress, projectName, user1):
    """adds message to db""" 
    tempMessage = Message(user = user1, name = projectName, progress = 0)
    tempMessage.save()

def addUser(name, address):
    user = User(username = name, email = address)
    user.save()