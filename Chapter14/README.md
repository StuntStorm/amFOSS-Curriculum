```
1. What three files do you need for EZSheets to access Google Sheets?
```
```
Answer:
> A credentials file named credentials-sheets. json.
> A token for Google Sheets named token-sheets. pickle.
> A token for Google Drive named token-drive. pickle.
```
-----------------------------------------------------
```
2. What two types of objects does EZSheets have?
```
```
Answer:
> Spreadsheet Objects

> Sheet Objects
```
-----------------------------------------------------
```
3. How can you create an Excel file from a Google Sheet spreadsheet?
```
```
Answer:
> Using downloadAsExcel() function
```
-----------------------------------------------------
```
4. How can you create a Google Sheet spreadsheet from an Excel file?
```
```
Answer:
> Using ezsheets.upload() function
```
-----------------------------------------------------
```
5. The ss variable contains a Spreadsheet object. What code will read data from the cell B2 in a sheet titled “Students”?
```
```
Answer:
> `class Data`
```
-----------------------------------------------------
```
6. How can you find the column letters for column 999?
```
```
Answer:
> Using ezsheets.getColumnLetterOf(999) function
```
-----------------------------------------------------
```
7. How can you find out how many rows and columns a sheet has?
```
```
Answer:
> Using sheet.rowCount for rows

> Using sheet.columnCount for columns
```
-----------------------------------------------------
```
8. How do you delete a spreadsheet? Is this deletion permanent?
```
```
Answer:
> Using delete() function, No it is not as it moves to the Trash section. But can be made permanent Delete passing True value for the argument
```
-----------------------------------------------------
```
9. What functions will create a new Spreadsheet object and a new Sheet object, respectively?
```
```
Answer:
> Using ezsheets.createSpreadsheet() function and Using ss.createSheet(), respectively
```
-----------------------------------------------------
```
10. What will happen if, by making frequent read and write requests with EZSheets, you exceed your Google account’s quota?
```
```
Answer:
> Yes, there is rate limit of 100 seconds for read and write on a Free Google Account.
```
-----------------------------------------------------
