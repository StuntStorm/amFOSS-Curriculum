import os
import openpyxl

def toTextFiles(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    for columnvalue in sheet.columns:
        with open('Convert-'+name+'.txt', 'w') as file:
            for cellvalue in columnvalue:
                file.write(cellvalue.value)

name = input("Enter File name : ")
toTextFiles(name+".xlsx")
