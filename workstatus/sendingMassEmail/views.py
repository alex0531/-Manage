# Create your views here.

from string import*
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from datetime import date
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives #
from django.template.loader import render_to_string #
from django.utils.html import strip_tags #
from workstatus.mail.models import *
import feedparser

import os, time
from datetime import date

    
    
def today():
    
    today = date.today()
    if today.isoweekday() == 4:
        if str(time.strftime('%X')) == '15:41:30':
            sendMorningMail()
            time.sleep(1)
            
    #elif today.isoweekday() == 6:
        if str(time.strftime('%X')) == '15:42:30':
            sendReminderMail()
            time.sleep(1)

    #return HttpResponse()

    
                
def sendMorningMail():
    template = get_template('Morning_Mail.html')
    
    subject, from_email, to = 'Morning Email (Reply to this Emailaddress ONLY!)', 'umanage.mpd@gmail.com', 'alex@myplanetdigital.com'
    
    html_content = render_to_string('Morning_Mail.html')
    text_content = strip_tags(html_content) #this strips the html, so people will have the text as well
    
    #Create the email, and attach the HTML version as well.
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    #return HttpResponse()    
    
 
def sendReminderMail():
    for user in User.objects.all():
        user_msgs = list(Message.objects.filter(user=user))
        
        #ssort by time
        
        if len(user_msgs) >0:        
            previous = user_msgs[len(user_msgs)-1].content
                
            template = get_template('Reminder_Mail.html')
            
            subject, from_email, to = 'Reminder Email (Reply to this Emailaddress ONLY!)', 'umanage.mpd@gmail.com', str(user.email) 
            html_content = render_to_string('Reminder_Mail.html',{'previous':previous})
            text_content = strip_tags(html_content) #this strips the html, so people will have the text as well
            
            #Create the email, and attach the HTML version as well.
            
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        
    #return HttpResponse()
