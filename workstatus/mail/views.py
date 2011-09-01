# Create your views here.
##workstatus>mail
#from string import*
#from django.http import HttpResponse
#from django.template import Context
#from django.template.loader import get_template
#import workstatus.mail.models
#from django.core.mail import send_mail
#from datetime import datetime
#
#import feedparser
#from django.contrib.auth.models import User
#from workstatus.mail.loaddb import addMessage, addUser
#from workstatus.mail.models import Message, User
#import time
#import smtplib
#
#Settings
#USERNAME="umanage.mpd@gmail.com"
#PASSWORD=" yashar2bananapeel"
#PROTO="https://"
#SERVER="mail.google.com"
#PATH="/gmail/feed/atom"
#
#getInitialFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
#lastModified = getInitialFeed.entries[0].modified
#ignoreList = []
#
################################################################################################################
#def read(request):
#    getInitialFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
#    lastModified = getInitialFeed.entries[0].modified
#    while True:
#        while True:
#            scrapedFeed = feedparser.parse(PROTO+USERNAME+":"+PASSWORD+"@"+SERVER+PATH)
#            try:
#                scrapedModified = scrapedFeed.entries[0].modified
#                break
#            except:
#                pass
#        if lastModified < scrapedModified:
#            lastModified=scrapedModified
#            name1 = scrapedFeed.entries[0].author_detail.name
#            email1 = scrapedFeed.entries[0].author_detail.email
#            try:
#                addUser(name1, email1)
#            except:
#                pass    
#            user = User.objects.get(email = email1)
#            content = str(scrapedFeed.entries[0].title)
#            time1 = str(scrapedModified) #parse into string so it can be sliced
#            time2 = time1[:10]+' '+time1[11:19] #edit string into a time that can be parsed
#            time3 = datetime.strptime(time2, '%Y-%m-%d %H:%M:%S') #parse string into a datetime object
#            addMessage(user, email1, content, time3)
#        
#        time.sleep(3)
#            
#    return HttpResponse()
################################################################################################################
#
#def parser(request):
#    """Filters through a message to find projects and their work progress status"""
#    """Example: What needs to get done: #Project1, #Project2, #Project"""
#
#    scrapedFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
#    length = 5
#    showEntries = []
#    
#    for i in range(length):
#        message = str(scrapedFeed.entries[i].title)
#        showEntries.append(message)
#
#    template = get_template('testing.html')
#    variables = Context({'showEntries':showEntries})
#    output = template.render(variables)
#
#    return HttpResponse(output)
#    
    
    