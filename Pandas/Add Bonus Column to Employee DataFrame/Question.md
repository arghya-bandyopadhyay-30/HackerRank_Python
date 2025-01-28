# Add Bonus Column to Employee DataFrame

## Problem Statement

A company plans to provide its employees with a bonus. 

Write a solution to create a new column `bonus` that contains the doubled values of the `salary` column.

## Input
A Pandas DataFrame `employees` with the following structure:

| Column Name | Type   |
|-------------|--------|
| name        | object |
| salary      | int    |

## Example

**Input:**
+---------+--------+
| name    | salary |
+---------+--------+
| Piper   | 4548   |
| Grace   | 28150  |
| Georgia | 1103   |
| Willow  | 6593   |
| Finn    | 74576  |
| Thomas  | 24433  |
+---------+--------+

**Output:**
+---------+--------+--------+
| name    | salary | bonus  |
+---------+--------+--------+
| Piper   | 4548   | 9096   |
| Grace   | 28150  | 56300  |
| Georgia | 1103   | 2206   |
| Willow  | 6593   | 13186  |
| Finn    | 74576  | 149152 |
| Thomas  | 24433  | 48866  |
+---------+--------+--------+

## Constraints
- The salary column contains only positive integers.
- The output should include a new column named bonus, where each value is double the corresponding salary value.
