```
1. What are the two values of the Boolean data type? How do you write them?
```
```
Answer:
> Two values of the Boolean data type are True and False. It is represented by T or F
```
---------------------------------------------------------
```
2. What are the three Boolean operators?
```
```
Answer:
> The three Boolean operators are "and", "not", "or".
```
---------------------------------------------------------
```
3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
```
```
Answer:
> AND Truth Table
|__________________________________|
| Expression      | Evaluates to   |
| :-------------  | :------------- |
| True and True   | True           |
| True and False  | False          |
| False and True  | False          |
| False and False | False          |
|__________________________________|

> OR Truth Table
|__________________________________|
| Expression      | Evaluates to   |
| :-------------  | :------------- |
| True and True   | True           |
| True and False  | True           |
| False and True  | True           |
| False and False | False          |
|__________________________________|

> NOT Truth Table
|__________________________________|
| Expression      | Evaluates to   |
| :-------------  | :------------- |
| Not True        | False          |
| Not False       | True           |
|__________________________________|

```
---------------------------------------------------------
```
4. What do the following expressions evaluate to?

(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)
```
```
Answer:
> False

> False

> True

> False

> False

> True
```
---------------------------------------------------------
```
5. What are the six comparison operators?
```
```
Answer:
> The Six Comparison Operators are:
- == - Equal To
- != - Not Equal To
- < - Less Than
- > - Greater Than
- <= - Less than or Equal to
- >= - Greater than or Equal to
```
---------------------------------------------------------
```
6. What is the difference between the equal to operator and the assignment operator?
```
```
Answer:
> The difference between the equal to operator (==) and the assignment operator (=) is that equal to operator is to check if the Boolean value is correct or not. Whereas assignment operator is to assign a value to the variable. Ex of Assignment Operator (x = 3), Ex of Equal To operator (n == 3).
```
---------------------------------------------------------
```
7. Explain what a condition is and where you would use one.
```
```
Answer:
> Condition is just a more specific name in the context of flow control statements. Conditions always evaluate down to a Boolean value, True or False.
> Almost every flow control statement uses a condition.
```
---------------------------------------------------------
```
8. Identify the three blocks in this code:

spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```
```
Answer:
> print('eggs')

> print('bacon')

> print('ham')
```
---------------------------------------------------------
```
9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
```
```
Answer:

spam = int(input())
if spam == 1:
    print('Hello')
elif spam == 2:
  print('Howdy')
else:
  print('Greetings!')
```
---------------------------------------------------------
```
10. What keys can you press if your program is stuck in an infinite loop?
```
```
Answer:
> Ctrl + c
```
---------------------------------------------------------
```
11. What is the difference between break and continue?
```
```
Answer:
> Break - program execution to break out of a while loop’s clause,When a program execution enters a loop, it will exit the loop only when a break statement is executed.

> Continue - When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and rechecks the loop’s condition.
```
---------------------------------------------------------
```
12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
```
```
Answer:
>  In a loop, when we take range(start, end, step) is the pattern.

> So, when it is range(10) it is actually range(0, 10)

> range(0, 10) The start point is 0 and end point is 10. but the value will be from 0 to 9 (if you want to include 10 as well then it should be range(0,11)).

> range(0,10,1) is the values from 0-9 but with 1 skip after every number.
```
---------------------------------------------------------
```
13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
```
```
Answer:
> Using Loop
for i in range(1,11):
    print(i)  


> Using while
i = 1
while(i<=10):
    print(i)
    i += 1
```
---------------------------------------------------------
```
14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
```
```
Answer:
> Yes, spam.bacon()
Common example : Math.sq()
```
---------------------------------------------------------
