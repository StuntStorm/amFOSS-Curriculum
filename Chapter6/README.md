```
1. What are escape characters?
```
```
Answer:
> An escape character is a backslash \ followed by the character you want to insert
```
-----------------------------------------------------
```
2. What do the \n and \t escape characters represent?
```
```
Answer:
> \n - New Line

> \t - Tab
```
-----------------------------------------------------
```
3. How can you put a \ backslash character in a string?
```
```
Answer:
> using of Raw string, It completely ignores all escape characters and prints any backslash that appears in the string
```
-----------------------------------------------------
```
4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it a problem that the single quote character in the word Howl's isn’t escaped?
```
```
Answer:
> It isn't a problem as double quotes are used on the start and end of the string so a single quote wont affect within this string
```
-----------------------------------------------------
```
5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
```
```
Answer:
> Multiline strings
```
-----------------------------------------------------
```
6. What do the following expressions evaluate to?

'Hello, world!'[1]
'Hello, world!'[0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]
```
```
Answer:
> 'e'

> 'Hello'

> 'Hello'

> 'lo world!
```
-----------------------------------------------------
```
7. What do the following expressions evaluate to?

'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()
```
```
Answer:
> 'HELLO'

> True

> 'hello'
```
-----------------------------------------------------
```
8. What do the following expressions evaluate to?

'Remember, remember, the fifth of November.'.split()
'-'.join('There can be only one.'.split())
```
```
Answer:
> ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

> 'There-can-be-only-one
```
-----------------------------------------------------
```
9. What string methods can you use to right-justify, left-justify, and center a string?
```
```
Answer:
> rjust() - right-justify

> ljust() - left-justify

> center() - center
```
-----------------------------------------------------
```
10. How can you trim whitespace characters from the beginning or end of a string?
```
```
Answer:
> lstrip() - beginning of a string/left of a string
> rstrip() - end of the string/right of a string
```
-----------------------------------------------------
