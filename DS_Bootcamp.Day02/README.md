## Intro to Python: OOP skills

This project was created as part of an educational module on object-oriented programming in Python. The goal is to master fundamental OOP principles through sequential task implementation - from basic class structure to building a modular project with logging and Telegram notifications.

The complete original version of the tasks can be found [here](README-full.md).

---

## Project Structure

### Exercise 00 — Simple class
Create a `Must_read` class that reads the `data.csv` file and outputs its contents. The code is placed directly in the class body without using methods.

### Exercise 01 — Method
Move the file reading code into a `file_reader()` method of the `Research` class, which returns the file contents.

### Exercise 02 — Constructor
Add an `__init__` constructor that accepts a file path. The `file_reader()` method uses this path. File structure error handling is mandatory.

### Exercise 03 — Nested class
The `file_reader()` method returns data as a list of lists. Add a nested `Calculations` class with `counts()` and `fractions()` methods for calculating values and proportions.

### Exercise 04 — Inheritance
Create an `Analytics` class that inherits from `Calculations`. Implement `predict_random()` and `predict_last()` methods.

### Exercise 05 — Config and the main program
Project structuring:
- `analytics.py` - core logic
- `config.py` - settings and report template
- `make_report.py` - main script  
Implement the `save_file()` method. Generate text reports.

### Exercise 06 — Logging
Add logging to all methods (to `analytics.log` file). Implement `send_telegram_message()` method for sending Telegram notifications.
