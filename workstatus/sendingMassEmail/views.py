# Create your views here.

from string import*
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives #
from django.template.loader import render_to_string #
from django.utils.html import strip_tags #


import feedparser

def sendmail(request):
    template = get_template('the_template.html')
    
    subject, from_email, to = 'Reply to this email ONLY!', 'umanage.mpd@gmail.com', 'alex@myplanetdigital.com'
    
    html_content = render_to_string('the_template.html')
    text_content = strip_tags(html_content) #this strips the html, so people will have the text as well
    
    #Create the email, and attach the HTML version as well.
    
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
     
    return HttpResponse()