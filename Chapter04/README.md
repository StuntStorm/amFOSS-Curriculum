```
1. What is []?
```
```
Answer:
> empty list [], the value [] is an empty list that contains no values, similar to '', the empty string.
```

```
2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
```
```
Answer:
> spam[2] = 'hello'
```

```
3. What does spam[int(int('3' * 2) // 11)] evaluate to? (spam = ['a', 'b', 'c', 'd'])
```
```
Answer:
> It gives out 'd'.
Explanation :
step 1 : '3' * 2 => 33
step 2 : 33//11 => 3
step 4 : spam[3] => 'd'
```

```
4. What does spam[-1] evaluate to?
```
```
Answer:
> 'd'
Explanation :
    -ve value goes backward.
```

```
5. What does spam[:2] evaluate to?
```
```
Answer:
> ['a', 'b']
Explanation :
step 1 : spam[start : end]
step 2 : spam[ : 2]
step 3 : so, spam[0] and spam[1] will be output
```

```
6. What does bacon.index('cat') evaluate to? (bacon = [3.14, 'cat', 11, 'cat', True])
```
```
Answer:
> 1
Explanation :
Indexing starts from 0,1,2,3....n
```

```
7. What does bacon.append(99) make the list value in bacon look like?
```
```
Answer:
> [3.14, 'cat', 11, 'cat', True, 99]
```

```
8. What does bacon.remove('cat') make the list value in bacon look like?
```
```
Answer:
> [3.14, 11, 'cat', True]
Explanation :
It always remove the first one. and wont delete the duplicate and it is in a unique and different position.
```

```
9. What are the operators for list concatenation and list replication?
```
```
Answer:
> The operator for list concatenation is +, while the operator for replication is *
```

```
10. What is the difference between the append() and insert() list methods?
```
```
Answer:
> insert() - Insert function we can add a specific element at a specified index of the list

> append() -  Append function we can add the element only at end of the list.
```

```
11. What are two ways to remove values from a list?
```
```
Answer:
> Using del statement

> Using remove()
```

```
12. Name a few ways that list values are similar to string values.
```
```
Answer:
> Both lists and strings can be passed to len(),
> have indexes and slices, be used in for loops,
> be concatenated or replicated,
> and be used with the in and not in operators.
```

```
13. What is the difference between lists and tuples?
```
```
Answer:
> Difference between Lists and Tuples respectively are:
 1. Mutable and Immutable
 2. Insertion and deletion best for Lists but tuples are appropriate for accessing the elements
 3. Have several built-in methods whereas for for tuple they dont have much built-in methods.
```

```
14. How do you type the tuple value that has just the integer value 42 in it?
```
```
Answer:
> tuple = (42)
```

```
15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
```
```
Answer:
> using list() function,
  Ex : List = list(Tuple)

> using tuple() function,
  Ex : Tuple = tuple(List)
```

```
16. Variables that ???contain??? list values don???t actually contain lists directly. What do they contain instead?
```
```
Answer:
> List values
```

```
17. What is the difference between copy.copy() and copy.deepcopy()?
```
```
Answer:
> The copy.copy(), can be used to make a duplicate copy of a mutable value like a list

> The deepcopy() function will copy the inner lists as well and a copy of a reference
```
