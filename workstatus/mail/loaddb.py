#from mail.models import*
import workstatus.mail.models
from models import Message, User

def addMessage(emailAddress, content, user, time):
    """adds message to db"""
    tempMessage = Message(emailAddress = emailAddress, user = user, content = content, time = time)
    tempMessage.save()

def addUser(name, address):
    user = User(username = name, email = address)
    user.save()