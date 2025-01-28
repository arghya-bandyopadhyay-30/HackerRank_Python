# Explanation of List Operations in Python

## Understanding the Problem

We are given a set of commands to manipulate a list. The list starts empty, and commands are executed sequentially.

### Command Breakdown

1. `insert i e`: Inserts element `e` at index `i`.
2. `print`: Prints the list.
3. `remove e`: Removes the first occurrence of `e`.
4. `append e`: Appends `e` to the end of the list.
5. `sort`: Sorts the list in ascending order.
6. `pop`: Removes the last element.
7. `reverse`: Reverses the list.

## Sample Walkthrough

For the sample input:
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


- `insert 0 5` → `[5]`
- `insert 1 10` → `[5, 10]`
- `insert 0 6` → `[6, 5, 10]`
- `print` → `[6, 5, 10]` (output)
- `remove 6` → `[5, 10]`
- `append 9` → `[5, 10, 9]`
- `append 1` → `[5, 10, 9, 1]`
- `sort` → `[1, 5, 9, 10]`
- `print` → `[1, 5, 9, 10]` (output)
- `pop` → `[1, 5, 9]`
- `reverse` → `[9, 5, 1]`
- `print` → `[9, 5, 1]` (output)

## Code Explanation

- We read `N`, the number of commands.
- We loop through `N` lines, splitting each command into `com` (command) and `args` (arguments).
- We use Python's `getattr()` function to dynamically call list methods, avoiding long `if-elif` conditions.
- `print` is handled separately since it doesn't modify the list.
