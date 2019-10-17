import os
import shutil

dir = os.getcwd()
subdir = dir+"/txt"
if os.path.exists(subdir)==False:
    os.mkdir(subdir)
filenames = os.listdir()

for fn in filenames:
    if fn.endswith(".doc") or fn.endswith(".docx"):
        pos = fn.rfind(".")
        newfn = fn[0:pos]
        newfn +=".txt"
        newfn = subdir+"/"+newfn
        f = open(newfn, "w")
        f.close();
        print(newfn)

        