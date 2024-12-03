# Advent of Code 2024 - Day 1: Historian Hysteria

## Problem Description

The Chief Historian has gone missing, and the Senior Historians needed my help to reconcile two lists of location IDs found in his office. To assist them, I solved two puzzles that involved analyzing these lists.

### Part 1: Total Distance Between Lists
For the first part, I calculated the total distance between two lists of location IDs by:  
1. Splitting the input into two separate lists of numbers based on their positions in the file.  
2. Sorting both lists to ensure the smallest numbers were paired first.  
3. Calculating the absolute difference for each pair of numbers and summing these differences to get the total distance.  

### Part 2: Similarity Score
The second part required me to calculate a similarity score by:  
1. Counting how many times each number in the first list appeared in the second list.  
2. Multiplying each number by its occurrence count in the second list.  
3. Summing these values to produce the final similarity score.  

This approach worked efficiently for the input data and provided the expected results.  

## My Results:
- **Part 1:** Total distance = `2904518`  
- **Part 2:** Similarity score = `18650129`  

## My Solution

I implemented the solution in Python using straightforward list operations. For Part 1, sorting the lists and iterating through them ensured that I could correctly pair the smallest numbers first. For Part 2, I used Python's `count` method to determine how often a number in the first list appeared in the second list, which made the calculations simple and effective.  

## How to Use

1. Clone the repository:  
   ```bash
   git clone https://github.com/f-ras/adventofcode2024.git
   ```
2. Navigate to the project directory:
   ```bash
   cd adventofcode2024/day01
   ```
3. Run the Python scripts for Part 1 and Part 2 to view the results.


## Notes
This solution is part of Advent of Code 2024, a fun programming challenge that releases daily puzzles leading up to Christmas.