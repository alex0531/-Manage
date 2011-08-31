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
from loaddb import addMessage, addUser
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
def read(request):
    while True:    
        while True:
            scrapedFeed = feedparser.parse(PROTO+USERNAME+":"+PASSWORD+"@"+SERVER+PATH)
            try:
                scrapedModified = scrapedFeed.entries[0].modified
                break
            except:
                pass
       
        if lastModified < scrapedModified:
            name = scrapedFeed.entries[0].name
            email = scrapedFeed.entries[0].email
            try:
                addUser(name, email)
            except:
                pass    
            user = User.objects.get(emailaddress = email)
            content = scrapedFeed.entries[0].title
            time1 = scrapedModified
            addMessage(user = user, emailaddress = email, time1 = time1, content = content)
        
        time.sleep(3)
        
    return HttpResponse()
################################################################################################################

def parser(request):
    """Filters through a message to find projects and their work progress status"""
    """Example: What needs to get done: #Project1, #Project2, #Project"""

    scrapedFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
    length = 5
    showEntries = []
    
    for i in range(length):
        message = str(scrapedFeed.entries[length-i-1].title)
        showEntries.append(message)

    template = get_template('testing.html')
    variables = Context({'showEntries':showEntries})
    output = template.render(variables)

    return HttpResponse(output)
    
    
    