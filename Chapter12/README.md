```
1. Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.
```
```
Answer:
> assert(spam >= 10, 'spam is less than 10.')
```
-----------------------------------------------------
```
2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
```
```
Answer:
> assert(eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!') or assert(eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!')
```
-----------------------------------------------------
```
3. Write an assert statement that always triggers an AssertionError.
```
```
Answer:
> assert(False, 'Error message : This assertion always triggers.')
```
-----------------------------------------------------
```
4. What are the two lines that your program must have in order to be able to call logging.debug()?
```
```
Answer:
> Code :
```
```
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')
```
```
```
-----------------------------------------------------
```
5. What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt
```
```
Answer:
> Code:
```
```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
```
```
```
-----------------------------------------------------
```
6. What are the five logging levels?
```
```
Answer:
> Info

> Debug

> Warning

> Error

> Critical
```
-----------------------------------------------------
```
7. What line of code can you add to disable all logging messages in your program?
```
```
Answer:
> logging.disable(logging.CRITICAL)
```
-----------------------------------------------------
```
8. Why is using logging messages better than using print() to display the same message?
```
```
Answer:
> Logging messages provides a timestamp and also disable certain functions on demand.
```
-----------------------------------------------------
```
9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
```
```
Answer:
> Step Over button will quickly execute the function call without stepping into it

> Step in button will cause the debugger to execute the next line of code and then pause again

> Step Out button will quickly execute the rest of the code until it steps out of the function it currently is in
```
-----------------------------------------------------
```
10. After you click Continue, when will the debugger stop?
```
```
Answer:
> It will stop when it has reached the end of the program or a line with a breakpoint.
```
-----------------------------------------------------
```
11. What is a breakpoint?
```
```
Answer:
> It is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.
```
-----------------------------------------------------
```
12. How do you set a breakpoint on a line of code in Mu?
```
```
Answer:
> We should right-click the line and select Set Breakpoint from the context menu
```
-----------------------------------------------------
