# Create your views here.
##workstatus>mail
from string import*
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import workstatus.mail.models
from django.core.mail import send_mail


import feedparser
import loaddb
from loaddb import addProject
from django.contrib.auth.models import User

import time
#import smtplib

#Settings
USERNAME="umanage.mpd@gmail.com"
PASSWORD=" yashar2bananapeel"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"


getInitialFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
lastModified = getInitialFeed.entries[0].modified
ignoreList = []

################################################################################################################
#def read(request):
#        while True:
#            scrapedFeed = feedparser.parse(PROTO+USERNAME+":"+PASSWORD+"@"+SERVER+PATH)
#            try:
#                scrapedModified = scrapedFeed.entries[0].modified
#                break
#            except:
#                pass
#        
#        if lastModified < scrapedModified:
#            #parser(request) --> need to bind to a variable because the parser function returns a value
#        
#        time.sleep(3)
################################################################################################################

def parser(request):
    """Filters through a message to find projects and their work progress status"""
    """Example: What needs to get done: #Project1, #Project2, #Project"""

    scrapedFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
    length = 5
    showEntries = [None]*length
    
    for i in range(length):
        message = str(scrapedFeed.entries[length-i-1].title)
        showEntries.insert(message,i)

    template = get_template('testing.html')
    variables = Context({'showEntries':showEntries})
    output = template.render(variables)
    
    send_mail('Subject here', 'Here is the message.', 'umanage.mpd@gmail.com', ['priscilla@myplanetdigital.com'], fail_silently=False)
   
    for name in startingPros: # add names of projects to database, name is a string
        fromAddress = str(scrapedFeed.entries[0].author_detail.email)
        fromName = str(scrapedFeed.entries[0].author_detail.name)
        for user in User.objects.all():
            if user.email == fromAddress or user.username == fromName:
                break
            else:
                user = User(username=str(scrapedFeed.entries[0].author_detail.name), email = fromAddress)
                user.save()
            addProject(fromAddress, name, user)

    return HttpResponse(output)