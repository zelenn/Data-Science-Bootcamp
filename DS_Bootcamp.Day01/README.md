# Intro to Python: Syntax and Semantics

This project is part of a learning module on Python programming fundamentals. The main goal is to master Python's syntax, basic data structures, and key language constructs through a series of sequential exercises.

The complete, original version of the tasks can be found [here](README-full.md).

---

## Project Structure

### Exercise 00 — Data types  
A function is created to define variables of eight built-in Python types: `int`, `str`, `float`, `bool`, `list`, `dict`, `tuple`, `set`. Types are displayed using the built-in `type()` function.

**Key objectives**:  
- Familiarization with basic data types;  
- Working with the `type` function and data output.  

---

### Exercise 01 — Working with files  
A script reads data from a CSV file and writes it in TSV format. Only external delimiters are processed, without altering string contents.

**Key objectives**:  
- Handling text files;  
- Understanding CSV vs. TSV structures;  
- Preserving data format integrity during conversion.  

---

### Exercise 02 — Search by key  
The program takes a company name as an argument and outputs its corresponding stock price. Uses two dictionaries: `COMPANIES` and `STOCKS`.

**Key objectives**:  
- Dictionary key lookup;  
- Command-line argument processing.  

---

### Exercise 03 — Search by value and by key  
Accepts a company ticker, returns its name and stock price. Implements reverse dictionary lookup by value.

**Key objectives**:  
- Reverse lookup in data structures;  
- Working with `.items()` and string formatting.  

---

### Exercise 04 — Dictionaries  
Creates a dictionary from a list of tuples where numeric values serve as keys and country lists as values. Data is output in a strictly specified format.

**Key objectives**:  
- Dictionary manipulation, including list values;  
- Using `setdefault()`.  

---

### Exercise 05 — Search by value or by key  
The program processes a comma-separated string of company names and tickers to determine input type. Output follows specified formatting rules.

**Key objectives**:  
- String and argument processing;  
- Dictionary operations and conditional logic;  
- Error handling for user input.  

---

### Exercise 06 — Sorting a dictionary  
Countries are sorted by numeric values in descending order. Equal values trigger secondary alphabetical sorting.

**Key objectives**:  
- Multi-criteria dictionary sorting;  
- Using `lambda` and `key` parameters.  

---

### Exercise 07 — Sets  
Processes email lists of customers, event participants, and mailing recipients. Uses set operations to solve three business tasks: identifying inactive customers, potential leads, and non-participating clients.

**Key objectives**:  
- Set operations;  
- Applying difference and intersection;  
- Implementing data filtering logic.  

---

### Exercise 08 — Working with strings as lists  
Two scripts are implemented:  
1. Converting email addresses into a `Name`, `Surname`, `E-mail` table;  
2. Generating personalized emails based on the table.  

**Key objectives**:  
- String parsing;  
- Working with delimiters and `capitalize`;  
- Formatted output using `f-strings`.  

---

### Exercise 09 — Caesar cipher  
Implements Caesar cipher for text encoding/decoding. Shift is specified numerically. Only Latin alphabet characters are processed; others are ignored.

**Key objectives**:  
- Using `ord()` and `chr()` for character operations;  
- Implementing cyclic shift with `modulo`;  
- Handling exceptions and non-standard input.  

--- 
