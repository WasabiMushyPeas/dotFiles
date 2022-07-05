import os
#from git import Repo


file = open("/home/jack/Documents/Scripts/Python/Automation/dataFiles/foldersAndFilesToBackUp.txt", "r")
lines = file.readlines()
file.close()

for line in lines:
    os.system("cp -r " + line.replace("\n", "") + " ~/Backup/dotFiles/")



#PATH_OF_GIT_REPO = r"~/Backup/dotFiles/.git/"  # make sure .git folder is properly configured
#COMMIT_MESSAGE = "comment from python script"


#repo = Repo(PATH_OF_GIT_REPO)
#repo.git.add(update=True)
#repo.index.commit(COMMIT_MESSAGE)
#origin = repo.remote(name='origin')
#origin.push()
