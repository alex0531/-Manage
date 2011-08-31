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
    #tempString = str(scrapedFeed.entries[0].title)
    tempString = str(scrapedFeed.entries[0].content)

    #00000000001111111111222222222233333333334444444444555555555566666666667777777777888888888899999
    #01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234
    
    startingKeys = ['started','began', 'initiated']
    doingKeys = ['working on', 'in progress','resume']
    doneKeys = ['completed','done','finished']
    keys = [startingKeys, doingKeys, doneKeys]

    startingPros = [] #store names of projects
    doingPros = [] 
    donePros = []
    projects = [startingPros,doingPros,donePros]

    startingTemp = [] #stores locations of keywords
    doingTemp = [] 
    doneTemp = []
    temp = [startingTemp, doingTemp,doneTemp]

    locate = [] #stores locations of key words

    #search for key words

    k = len(keys)

    for i in range(k):
        for j in range(len(keys[i])):
            x = find(tempString,keys[i][j])
            while x != -1:
                locate.append(x)
                temp[i].append(x)
                x = find(tempString,keys[i][j],x+1)

##    for i in range(len(temp)):
##        for x in range(len(temp[i])):
##            print temp[i][x]

    locate.sort()
    #print 'locate, sorted:',locate,'\n'

    #search for hash tags after each keyword location

    for i in range (k):
        for j in range(len(temp[i])):
            start = temp[i][j] #location of keyword
            n = locate.index(start) #index of location in the locate list
            #print n
            #print 'locate [ n ] = start'
            #print 'locate [',n,'] =',start
            if (n == len(locate)-1):
                end = len(tempString)
            else:
                end = locate[n+1]
            #print 'end',end
            x = find(tempString, '#', start)
            #print 'x ',x
            while x!= -1 and x < end: #while a hash tag can be found
                sub = ''
                x+=1
                #print tempString[x],ord(tempString[x])
                while (tempString[x] in ascii_letters):
                    #while next space, period, comma etc is not reached yet
                    #while next space, period, comma etc is not reached yet
                    sub += tempString[x]
                    #print 'sub:',sub
                    x += 1
                projects[i].append(sub) #add project name to list
                #print projects[i]
                start = x+1
                x = find(tempString, '#', start)

    template = get_template('testing.html')
    variables = Context({'tempString': tempString, 'startingPros': startingPros, 'doingPros': doingPros, 'donePros': donePros, 'pausePros': pausePros})
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
    
    
    
   
    

