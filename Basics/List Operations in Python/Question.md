# List Operations in Python

## Problem Statement

Consider a list (`list = []`). You can perform the following commands:

- `insert i e`: Insert integer `e` at position `i`.
- `print`: Print the list.
- `remove e`: Delete the first occurrence of integer `e`.
- `append e`: Insert integer `e` at the end of the list.
- `sort`: Sort the list.
- `pop`: Remove the last element from the list.
- `reverse`: Reverse the list.

Initialize an empty list and read an integer `N`, which represents the number of commands to be executed. Then, execute the commands as per the given instructions.

## Input Format

- The first line contains an integer, `N`, denoting the number of commands.
- Each of the next `N` lines contains one of the commands from the list above.

## Constraints

- The elements added to the list must be integers.

## Output Format

- For each `print` command, print the list on a new line.

### Sample Input
```
12 
insert 0 5 
insert 1 10 
insert 0 6 
print 
remove 6 
append 9 
append 1 
sort 
print 
pop 
reverse 
print
```

### Sample Output
```
[6, 5, 10] 
[1, 5, 9, 10] 
[9, 5, 1]
```



