```
1. Does PyInputPlus come with the Python Standard Library?
```
```
Answer:
> No, We have to import that module
```
-----------------------------------------------------
```
2. Why is PyInputPlus commonly imported with import pyinputplus as pyip?
```
```
Answer:
> To shorten it, so that everytime we dont have to use the whole `pyinputplus` instead we can use `pyip`
Example : pyip.inputInt(prompt='Enter a number: ') instead of pyinputplus.inputInt(prompt='Enter a number: ')
```
-----------------------------------------------------
```
3. What is the difference between inputInt() and inputFloat()?
```
```
Answer:
> inputInt() - which accept int numbers

> inputFloat() - which accept float numbers
```
-----------------------------------------------------
```
4. How can you ensure that the user enters a whole number between 0 and 99 using PyInputPlus?
```
```
Answer:
> inputNum() Ensures the user enters a number and returns an int or float, depending on if the number has a decimal point in it
```
-----------------------------------------------------
```
5. What is passed to the allowRegexes and blockRegexes keyword arguments?
```
```
Answer:
> allowReegexes : pyip.inputNum(allowRegexes=[r' '])

> blockRegexes : pyip.inputNum(blockRegexes=[r' '])
```
-----------------------------------------------------
```
6. What does inputStr(limit=3) do if blank input is entered three times?
```
```
Answer:
> By default, blank input isn’t allowed unless the blank keyword argument is set to True:

> But if it is true, the value will be ''
```
-----------------------------------------------------
```
7. What does inputStr(limit=3, default='hello') do if blank input is entered three times?
```
```
Answer:
> 'hello'
```
-----------------------------------------------------
