import os
import csv
import openpyxl


direc = input("Enter the Directory : ")
for excelFile in os.listdir(direc):
    if not excelFile.endswith('xlsx'):
        continue

    wb = openpyxl.load_workbook(excelFile)

    for sheetName in wb.sheetnames:
        sheet = wb["sheetname"]
        csvFilename = excelFile.split('.')[0]+'_'+sheet.title+'.csv'
        csvFileObj = open(csvFilename, 'w', newline='')

        csvWriter = csv.writer(csvFileObj)

        for rowObj in sheet.rows:
            rowData = []
            for cellObj in rowObj:
                rowData.append(cellObj.value)
            csvWriter.writerow(rowData)
        csvFileObj.close()
