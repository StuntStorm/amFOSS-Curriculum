import os

def getDirSize(start_path):
    size = 0
    for folderName, subFolder, filename in os.walk(start_path):
        for file in filename:
            filePath = os.path.join(folderName, file)
            size += os.path.getsize(filePath)


    return size

folderPath = input("Enter Folder Path : ")
rejectSize = int(input("Enter RejectSize : "))
root = os.path.abspath(folderPath)

for doc in os.listdir(root):
    docPath = os.path.join(root, doc)
    if os.path.isdir(docPath):
        size = getDirSize(docPath)
    else:
        size = os.path.getsize(docPath)
    if size > rejectSize:
        print(f'{docPath}: {size}')
