# Advent of Code 2024 - Day 2: Red-Nosed Reports  

## Problem Description  

At the Red-Nosed Reindeer reactor, I was tasked with analyzing unusual data reports to determine their safety. Each report contained a series of levels, and the safety rules were as follows:  

1. Levels must either be strictly increasing or strictly decreasing.  
2. The difference between any two adjacent levels must be between 1 and 3.  

### Part 1: Counting Safe Reports  
To solve the first part:  
- I read the reports and evaluated them against the safety rules.  
- A report was marked safe if it followed a consistent trend (increasing or decreasing) and satisfied the difference constraint for all adjacent levels.  

### Part 2: Accounting for the Problem Dampener  
In the second part, the engineers introduced a Problem Dampener. This allowed me to ignore a single "bad" level in each report. If removing one level would make an unsafe report safe, it was counted as safe.  
- I adjusted my analysis to simulate the removal of each level in an unsafe report.  
- If removing any level resulted in a safe report, I marked the entire report as safe.  

## Results  

- **Part 1:** Number of safe reports = `639`  
- **Part 2:** Number of safe reports (with Problem Dampener) = `674`  

## My Solution  

The solution was implemented in Python and is divided into three main files:  
- **`part1.py`:** Contains the logic for analyzing the reports and counting the safe ones based on the original safety rules.  
- **`part2.py`:** Builds on Part 1 by incorporating the Problem Dampener logic to allow for one level removal.  
- **`utils.py`:** Includes helper functions to parse and evaluate the reports, such as checking trends and adjacent level differences.  

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

## Notes
This solution is part of Advent of Code 2024, a fun programming challenge that releases daily puzzles leading up to Christmas.