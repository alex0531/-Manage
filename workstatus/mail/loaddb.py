#from mail.models import*
import models
from models import Project, User

def addProject(emailAddress, projectName, user1):
    """adds project to db""" 
    tempProject = Project(user = user1, name = projectName, progress = 0)
    tempProject.save()

def updateProject(emailAddress, projectName, progress):
    """updates status of project in db"""
    doingKeys = ['working on', 'in progress','resume']
    doneKeys = ['completed','done','finished']
    pauseKeys = ['pause','on hold']
    
    user = User.objects.get(email=emailAddress)
    
    if progress in doingKeys:
        progress = 0
    elif progress in pauseKeys:
        progress = 1
    elif progress in doneKeys:
        progress = 2
    else:
        print "Keyword not found."
        return None
    
    user.save()