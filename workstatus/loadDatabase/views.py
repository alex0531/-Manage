# Create your views here.
from loadDatabase.models import*

def addProject(emailAddress, projectName):
       
    tempProject = Project(user = user, projectName = projectName, progress = 0)
    tempProject.save()

def updateProject(emailAddress, projectName, progress):
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