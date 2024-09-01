pyinstaller --onefile pphrcp.py


"c:/Program Files (x86)/Windows Kits/10/App Certification Kit/signtool" sign /n "Dolno" /tr http://time.certum.pl/ /td SHA256 /fd SHA256 /v dist\pphrcp.exe

