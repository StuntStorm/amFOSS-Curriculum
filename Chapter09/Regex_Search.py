import os
import re

regex = input('Enter Regex: ')
folderPath = input('Enter FolderPath : ')

if not os.path.isdir(folderPath):
    print('Input a Folder path')

userRegex = re.compile(regex)

for filename in os.listdir(folderPath):

    if filename.endswith('.txt'):

        with open(filename) as file:

            for line in file:
                mo = userRegex.search(line)

                if mo:
                    print(line, end='')
