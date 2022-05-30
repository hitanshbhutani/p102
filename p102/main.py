import shutil
import os
from_dir = "C:/Users/Hitansh/Downloads"
to_dir = "C:/Users/Hitansh/Desktop/documents"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for i in list_of_files:
    name, extension = os.path.splitext(i)
    if extension == "":
        continue
    if extension in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir+'/' + i
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + i
if os.path.exists(path2):
    print("moving " + i + "....")
    shutil.move(path1, path3)
else:
    os.makedirs(path2)
    print("moving " + i + "....")
    shutil.move(path1, path3)
