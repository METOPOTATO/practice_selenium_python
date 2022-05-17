from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


gauth = GoogleAuth()


gauth.LocalWebserverAuth()	
drive = GoogleDrive(gauth)


f = drive.CreateFile({'title': 'test'})
f.SetContentFile('/home/admin/Desktop/Python/practice_selenium_python/note.txt')
f.Upload()

f = None
