# Advent of Code - Day 3: Mull It Over  

## Problem Description  

The task involved analyzing corrupted memory to extract valid `mul(X, Y)` instructions and calculate the sum of their results.  

### Part 1:  
Identify and process uncorrupted `mul(X, Y)` instructions from the corrupted memory. Invalid characters and improperly formatted instructions were ignored.  

### Part 2:  
Handle conditional instructions (`do()` and `don't()`) that enable or disable subsequent `mul` instructions. Only the enabled `mul` instructions were processed for the final sum.  

## Solution Overview  

### Part 1:  
- Extract all valid `mul(X, Y)` instructions using the helper function `extract_mul_uncorrupted_instructions`.  
- Parse each valid instruction to retrieve values `X` and `Y`, then calculate their product.  
- Sum the results of all valid `mul` instructions.  

### Part 2:  
- Extract both `mul(X, Y)` and conditional instructions (`do()`/`don't()`) using `extract_uncorrupted_instructions_complete`.  
- Track the current state (`do` or `don't`) and filter out disabled `mul` instructions.  
- Calculate the sum of results from only the enabled `mul` instructions.  

## How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/f-ras/adventofcode2024.git
   ```
2. Navigate to the project directory:
   ```bash
   cd adventofcode2024/day01
   ```
3. Run the scripts for each part:  
   - **Part 1:**  
     To count the number of safe reports based on the original safety rules, run:  
     ```bash
     python part1.py
     ```  
   - **Part 2:**  
     To count the number of safe reports using the Problem Dampener logic, run:  
     ```bash
     python part2.py
     ```

## File Descriptions  

- **`input.txt`**: The corrupted memory data (puzzle input).  
- **`extractions.py`**: Utility functions to extract valid instructions:  
  - `extract_mul_uncorrupted_instructions`: Finds valid `mul(X, Y)` instructions.  
  - `extract_uncorrupted_instructions_complete`: Extracts both `mul` and conditional instructions.  
- **`part1.py`**: Script to solve Part 1 by summing the results of valid `mul(X, Y)` instructions.  
- **`part2.py`**: Script to solve Part 2 by processing conditional instructions (`do()` and `don't()`) and summing the results of enabled `mul(X, Y)` instructions.  

## Results  

- **Part 1 Output:** `173517243`  
- **Part 2 Output:** `100450138`