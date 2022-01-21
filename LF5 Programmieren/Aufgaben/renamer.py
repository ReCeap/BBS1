import os

folderpath = r"C:\Users\ReGul4r\Desktop\ranks\old"

filepath = (os.path.join(root, filename)
            for root , _, filenames in os.walk(folderpath)
            for filename in filenames)

a=0

for path in filepath:
    newname = "gold" + str(a)+".png"
    a+=1
    if newname != path:
        os.rename(path, newname)