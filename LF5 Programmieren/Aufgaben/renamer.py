import os

folderpath = r"C:\Users\admin\Documents\Schule\BBS1\LF5 Programmieren\Aufgaben"

filepath = (os.path.join(root, filename)
            for root , _, filenames in os.walk(folderpath)
            for filename in filenames)

for path in filepath:
    newname = path.replace("K9_", "")
    if newname != path:
        os.rename(path, newname)