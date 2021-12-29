import openpyxl

def invertCells(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    newSheet = wb.create_sheet(index=0, title='inverted')
    for rowObj in sheet.rows:
        for cellObj in rowObj:
            colIndex = cellObj.column
            rowIndex = cellObj.row
            newSheet.cell(row=colIndex, column=rowIndex).value = cellObj.value
    wb.save('invert_'+filename)

invert = input("Enter the File name along with Extension : ")
invertCells(invert)
