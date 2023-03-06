import os
f=open("copy_files_only.bat",'w')
f.write("xcopy ")
f.write(input("Enter source address")+" ")
f.write(input("Enter destination address"))
f.close()
os.startfile("copy_files_only.bat")
