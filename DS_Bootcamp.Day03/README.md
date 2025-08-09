# Intro to Python: Package management and virtual environment

This project was completed as part of a Python learning module, focusing on practical skills with libraries, virtual environments, web scraping, profiling, and unit testing.

Tasks are implemented step-by-step: from creating a virtual environment to writing a Yahoo Finance parser, performance optimization, and creating automated tests.

The full version of task requirements can be found in [this document](README-full.md)

---

## Project Structure

### Exercise 00 — Virtual Environment  
Create a virtual environment named after the user. The `venv.py` script prints the path to the currently active environment using the `os` library.

### Exercise 01 — Package Installation  
Install and use the `termgraph` library for terminal data visualization. Created `pies_bars.sh` to generate colored charts from CSV data.

### Exercise 02 — Multiple Library Installation  
The `librarian.py` script installs `BeautifulSoup` and `PyTest` via `requirements.txt`, verifies it's running in the correct environment, and archives it.  

Also outputs installed libraries in the format:
```
soupsieve==2.6
termgraph==...
typing_extensions==...
```

### Exercise 03 — Very Beautiful Soup  
Created `financial.py` script that scrapes [Yahoo Finance](https://finance.yahoo.com/quote/MSFT/financials?p=MSFT) to extract company financials by ticker and field name. Uses `requests`, `BeautifulSoup`, `time.sleep`.

Example execution:  
```bash
./financial.py 'MSFT' 'Total Revenue'
('Total Revenue', '261,802,000', '245,122,000', ...)
```

### Exercise 04 — Profiling  
Conducted performance profiling of scripts:

- `profiling-sleep.txt` — with `time.sleep(5)`
- `profiling-tottime.txt` — without `sleep`, sorted by `tottime`
- `profiling-http.txt` — using `httpx` instead of `requests`
- `profiling-ncalls.txt` — sorted by call count
- `pstats-cumulative.txt` — top-5 functions by cumulative time using `pstats`

### Exercise 05 — Testing  
Created `financial_test.py` with `PyTest` tests. Verifies:

- Whether the function returns correct values for given field and ticker
- If the result is a tuple
- Whether it raises exceptions for invalid tickers or fields
