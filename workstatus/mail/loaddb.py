#from mail.models import*
from workstatus.mail.models import Message, User

def addMessage(user, email1, content, time1):
    """adds message to db"""
    tempMessage = Message(user = user, emailaddress = email1, content = content, time1 = time1)
    tempMessage.save()

def addUser(name, address):
    user = User(username = name, email = address)
    user.save()