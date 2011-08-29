# Create your views here.
##workstatus>mail
from string import*
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.core.mail import send_mail


import feedparser
#import time
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


# Continually check gmail

#Matt's serial port
#SERIALPORT = "COMn"

#Max's serial port
#SERIALPORT = "/dev/tty.usbmodem1d11" 

#UBUNTU server serial port
#SERIALPORT = "/dev/ttyACM0"

#Email setup

#def sendEmail(replyAddress, msg):
#	fromaddr = 'umanage.mpd@gmail.com'  
#	toaddrs  = replyAddress + '@gmail.com'  
#	msg = 'Sorry, the subject of your email did not make sense. :('  
#	  
#	# Credentials (if needed) 
#	username = 'umanage.mpd@gmail.com'  
#	password = 'yashar2bananapeel'  
#	  
#	# The actual mail send  
#	server = smtplib.SMTP('smtp.gmail.com:587')  
#	server.starttls()  
#	server.login(username,password)  
#	server.sendmail(fromaddr, toaddrs, msg)  
#	server.quit()  
#
#
## Set up serial port
##try:
##	ser = serial.Serial(SERIALPORT, 9600)
##except serial.SerialException:
##	print "no device connected - exiting"
##	sys.exit()
#
##Setup initial state - if there are emails before script is initiated they will be ignored
#getInitialFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
#lastModified = getInitialFeed.entries[0].modified #returns an integer
#ignoreList = []
#
## Continually check gmail
#while True:
#	#
#	while True:
#		scrapedFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)

#                print "Title: "+str(scrapedFeed.entries[0].title)
#		try:
#			scrapedModified = scrapedFeed.entries[0].modified                        
#                        print 1
#			break
#		except:
#			pass
#	print "The last iteration's time value: " + lastModified
#	print "The current iteration's time value: "  + scrapedModified  
#	  
#	#Compare the previous's iteration 'modified value' with the current iteration's
#	if lastModified < scrapedModified:
#		print " Inside first if - The last iteration's time value: " + lastModified
#		print "Inside first if  - The current iteration's time value: "  + scrapedModified 
#		print 2
#
#		lastModified = scrapedModified
#
#		#check for secret passcode
#		if str(scrapedFeed.entries[0].title).lower() == 'herp':	
#			# Output data to serial port 
#			#ser.write("m")
#			print "opening garage door"
#                        print 3
#		
#		else:
#			print "access denied using passcode " + scrapedFeed.entries[0].title
#			accessDeniedEmail(scrapedFeed.entries[0].author_detail.email)
#
#			#ignoreList
#	else: 
#		#ser.write("n")
#		print "waiting for instructions"
#		
#		#print 2

#		try:
#			scrapedModified = scrapedFeed.entries[0].modified #returns an integer
#			break
#		except:
#			pass
#	# print "The last iteration's time value: " + lastModified
#	# print "The current iteration's time value: "  + scrapedModified  
#	  
#	#Compare the previous's iteration 'modified value' with the current iteration's
#	if lastModified < scrapedModified: #if there are more unread messages
#		#print " Inside first if - The last iteration's time value: " + lastModified
#		#print "Inside first if  - The current iteration's time value: "  + scrapedModified 
#		# print 1
#
#		lastModified = scrapedModified
#		
#
#		#check for secret passcode
#		#if str(scrapedFeed.entries[0].title).lower() == 'herp':	
#		#	# Output data to serial port 
#		#	#ser.write("m")
#		#	#print "opening garage door"
#		#
#		#else:
#		#	print "access denied using passcode " + scrapedFeed.entries[0].title
#		#	accessDeniedEmail(scrapedFeed.entries[0].author_detail.email)
#		#
#		#	#ignoreList
#	#else: 
#	#	ser.write("n")
#	#	print "waiting for instructions"
#		
#		# print 2

#
#
#	
#	#To avoid any potential timeout issues
#	time.sleep(3)


################################################################################################################

def parser(request):
    scrapedFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
    

    """Filters through a message to find projects and their work progress status"""
    tempString = str(scrapedFeed.entries[0].title)

    #tempString = str(scrapedFeed.entries[0].title)

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

    template = get_template('testing.html')


    variables = Context({'tempString': tempString, 'startingPros': startingPros, 'doingPros': doingPros, 'donePros': donePros, 'pausePros': pausePros})
    
    output = template.render(variables)
    
    #send_mail('hello','testing django core mail','umanage.mpd@gmail.com',['priscilla@myplanetdigital.com'],fail_silently=False,auth_user='umanage.mpd@gmail.com',auth_password='yashar2bananapeel',connection=None)
    #sendEmail('priscilla@myplanetdigital.com')

    return HttpResponse(output)
#
#def sendEmail(replyAddress):
#	fromaddr = 'umanage.mpd@gmail.com'  
#	toaddrs  = replyAddress # + '@hotmail.com'  
#	msg = 'Sorry, that passcode is incorrect'  
#	  
#	# Credentials (if needed) 
#	username = 'umanage.mpd@gmail.com'  
#	password = 'yashar2bananapeel'  
#	  
#	# The actual mail send  
#	server = smtplib.SMTP('smtp.gmail.com:587')  
#	server.starttls()  
#	server.login(username,password)  
#	server.sendmail(fromaddr, toaddrs, msg)  
#	server.quit()  
   
    

