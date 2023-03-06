import os
f=open("move_files_only.bat",'w')
f.write("move ")
f.write(' "'+input("Enter source address")+'" ')
f.write('"'+input("Enter destination address")+'"')
f.close()
os.startfile("move_files_only.bat")
