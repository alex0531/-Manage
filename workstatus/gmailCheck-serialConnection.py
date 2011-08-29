"""
This python script needs to be run on a laptop connected to the arduino via serial port.
It will check gmail for a new email, check if it meets the credentials required, and if so
send the character 'm' via serial port to the arduino.
"""


import serial, sys
import feedparser
import time
import smtplib  

#Settings
USERNAME="90cgaragedoor@gmail.com"
PASSWORD=" yashar2bananapeel"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"

#Matt's serial port
#SERIALPORT = "COMn"

#Max's serial port
SERIALPORT = "/dev/tty.usbmodem1d11" 

#UBUNTU server serial port
#SERIALPORT = "/dev/ttyACM0"

#Email setup

def accessDeniedEmail(replyAddress):
	fromaddr = '90cgaragedoor@gmail.com'  
	toaddrs  = replyAddress + '@gmail.com'  
	msg = 'Sorry, that passcode is incorrect'  
	  
	# Credentials (if needed) 
	username = '90cgaragedoor@gmail.com'  
	password = 'yashar2bananapeel'  
	  
	# The actual mail send  
	server = smtplib.SMTP('smtp.gmail.com:587')  
	server.starttls()  
	server.login(username,password)  
	server.sendmail(fromaddr, toaddrs, msg)  
	server.quit()  


# Set up serial port
try:
	ser = serial.Serial(SERIALPORT, 9600)
except serial.SerialException:
	print "no device connected - exiting"
	sys.exit()

#Setup initial state - if there are emails before script is initiated they will be ignored
getInitialFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
lastModified = getInitialFeed.entries[0].modified
ignoreList = []

# Continually check gmail
while True:
	#
	while True:
		scrapedFeed = feedparser.parse(PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH)
		try:
			scrapedModified = scrapedFeed.entries[0].modified
			break
		except:
			pass
	# print "The last iteration's time value: " + lastModified
	# print "The current iteration's time value: "  + scrapedModified  
	  
	#Compare the previous's iteration 'modified value' with the current iteration's
	if lastModified < scrapedModified:
		#print " Inside first if - The last iteration's time value: " + lastModified
		#print "Inside first if  - The current iteration's time value: "  + scrapedModified 
		# print 1

		lastModified = scrapedModified

		#check for secret passcode
		if str(scrapedFeed.entries[0].title).lower() == 'herp':	
			# Output data to serial port 
			ser.write("m")
			print "opening garage door"
		
		else:
			print "access denied using passcode " + scrapedFeed.entries[0].title
			accessDeniedEmail(scrapedFeed.entries[0].author_detail.email)

			#ignoreList
	else: 
		ser.write("n")
		print "waiting for instructions"
		
		# print 2



	
	#To avoid any potential timeout issues
	time.sleep(3)


# Close serial port
ser.close()



#Todo list
# - Read authenticated users from mySQL database
# - Add authenticated users via django
# - GPS apps
 
