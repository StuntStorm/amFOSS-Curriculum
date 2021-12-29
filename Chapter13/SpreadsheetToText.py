import os
import openpyxl

def toTextFiles(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    for colObj in sheet.columns:
        with open('Convert-'+name+'.txt', 'w') as file:
            for cellObj in colObj:
                file.write(cellObj.value)

name = input("Enter File name : ")
toTextFiles(name+".xlsx")
