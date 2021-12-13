```
1. What does the code for an empty dictionary look like?
```
```
Answer:
> {}
```
-----------------------------------------------------
```
2. What does a dictionary value with a key 'foo' and a value 42 look like?
```
```
Answer:
> {'foo': 42}
```
-----------------------------------------------------
```
3. What is the main difference between a dictionary and a list?
```
```
Answer:
> Dictionary elements are accessed using key-values and the keys of dictionary can be of any data type.

> List elements are accessed using indexing and the indexing of list are integers starting from 0
```
-----------------------------------------------------
```
4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
```
```
Answer:
> Trying to access a key that does not exist in a dictionary will result in a KeyError error message, much like a list’s “out-of-range” IndexError error message.
```
-----------------------------------------------------
```
5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
```
```
Answer:
> 'cat' in spam states that there is the string value called cat in the spam dictionary.

> 'cat' in spam.keys() states that there is a key named cat.
```
-----------------------------------------------------
```
6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
```
```
Answer:
> 'cat' in spam checks whether there is a 'cat' key in the dictionary

> 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam
```
-----------------------------------------------------
```
7. What is a shortcut for the following code?

if 'color' not in spam:
    spam['color'] = 'black'
```
```
Answer:
> spam.setdefault('color', 'black')
```
-----------------------------------------------------
```
8. What module and function can be used to “pretty print” dictionary values?
```
```
Answer:
> pprint.pprint()
```
-----------------------------------------------------
