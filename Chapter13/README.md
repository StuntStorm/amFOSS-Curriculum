```
1. What does the openpyxl.load_workbook() function return?
```
```
Answer:
> openpyxl.load_workbook() function takes in the filename and returns a value of the workbook data type
```
-----------------------------------------------------
```
2. What does the wb.sheetnames workbook attribute contain?
```
```
Answer:
> wb.sheetnames - List of all the sheet names in the workbook
```
-----------------------------------------------------
```
3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?
```
```
Answer:
> wb['Sheet1']
```
-----------------------------------------------------
```
4. How would you retrieve the Worksheet object for the workbook’s active sheet?
```
```
Answer:
> wb.active
```
-----------------------------------------------------
```
5. How would you retrieve the value in the cell C5?
```
```
Answer:
> sheet['C5']
```
-----------------------------------------------------
```
6. How would you set the value in the cell C5 to "Hello"?
```
```
Answer:
> sheet['C5'] = "Hello"
```
-----------------------------------------------------
```
7. How would you retrieve the cell’s row and column as integers?
```
```
Answer:
> sheet.cell(row=1, column=2)
```
-----------------------------------------------------
```
8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?
```
```
Answer:
> sheet.max_column attribute is an integer - Gets the highest column number

> sheet.max_row attribute is an integer - Gets the highest row number
```
-----------------------------------------------------
```
9. If you needed to get the integer index for column 'M', what function would you need to call?
```
```
Answer:
> column_index_from_string('M')
```
-----------------------------------------------------
```
10. If you needed to get the string name for column 14, what function would you need to call?
```
```
Answer:
> get_column_letter(14)
```
-----------------------------------------------------
```
11. How can you retrieve a tuple of all the Cell objects from A1 to F1?
```
```
Answer:
> tuple(sheet['A1':'F1'])
```
-----------------------------------------------------
```
12. How would you save the workbook to the filename example.xlsx?
```
```
Answer:
> wb.save('example.xlsx')
```
-----------------------------------------------------
```
13. How do you set a formula in a cell?
```
```
Answer:
> Using openpyxl module
```
-----------------------------------------------------
```
14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?
```
```
Answer:
> Use the openpyxl module to programmatically add formulas to cells, just like any normal value
```
-----------------------------------------------------
```
15. How would you set the height of row 5 to 100?
```
```
Answer:
> sheet.row_dimensions[5].height = 100
```
-----------------------------------------------------
```
16. How would you hide column C?
```
```
Answer:
> Right Click the Column C and Hide it
```
-----------------------------------------------------
```
17. What is a freeze pane?
```
```
Answer:
> Freeze pane - Frozen column or row headers, that are always visible to the user even as they scroll through the spreadsheet
```
-----------------------------------------------------
```
18. What five functions and methods do you have to call to create a bar chart?
```
```
Answer:
> Create a Reference object from a rectangular selection of cells.

> Create a Series object by passing in the Reference object.

> Create a Chart object.

> Append the Series object to the Chart object.

> Add the Chart object to the Worksheet object, optionally specifying which cell should be the top-left corner of the chart
```
-----------------------------------------------------
