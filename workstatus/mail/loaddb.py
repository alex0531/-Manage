#from mail.models import*
import workstatus.mail.models
from models import Message, User

def addMessage(email1, content, user, time1):
    """adds message to db"""
    tempMessage = Message(emailaddress = email1, content = content, user = user, time1 = time1)
    tempMessage.save()

def addUser(name, address):
    user = User(username = name, email = address)
    user.save()