# Create your views here.
##workstatus>mail
from string import*
from django.http import HttpResponse

def helloworld(request):
    output = '<html><head><title>Hello World!</title></head><body><h1>Hello World!</h1></body>'
    return HttpResponse(output)

def parser(request):
    """Filters through a message to find projects and their work progress status"""
    
    tempString = "I started #giveMattMoney. I am working on #jelly and #this. I paused #project. I am done #lunch, #dinner, and #breakfast."
             #00000000001111111111222222222233333333334444444444555555555566666666667777777777888888888899999
             #01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234

    startingKeys = ['started','began', 'initiated']
    doingKeys = ['working on', 'in progress','resume']
    doneKeys = ['completed','done','finished']
    pauseKeys = ['pause','on hold']
    keys = [startingKeys, doingKeys, doneKeys, pauseKeys]

    startingPros = [] #store names of projects
    doingPros = [] 
    donePros = []
    pausePros = []
    projects = [startingPros,doingPros,donePros,pausePros]

    startingTemp = [] #stores locations of keywords
    doingTemp = [] 
    doneTemp = []
    pauseTemp = []
    temp = [startingTemp, doingTemp,doneTemp,pauseTemp]

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
    output = "This is the message: \n" + tempString
    This is the message:<br>
    #These are the projects added
    #print startingPros
    #print '\nThese are the projects in progress:'
    #print doingPros
    #print '\nThese are the projects that are finished:'
    #print donePros
    #print '\nThese are the projects that have been paused:'
    #print pausePros"""

    return HttpResponse(output)
    

