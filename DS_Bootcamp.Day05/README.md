# Pandas: Working with DataFrames

This project was developed as part of a Python fundamentals module, focusing on usind Pandas library.

The complete task specifications are available in [this document](README-full.md)


## Project Structure

### 00: Load and Save
- Read CSV with specific row filtering
- Clean datetime index
- Save with custom delimiter
- Handle header/footer skips

### 01: Basic Operations
- DateTime feature extraction
- Time-of-day categorization
- Statistical analysis:
  - Counts/value_counts
  - Min/max hours
  - Mode calculation
  - Early/late visitor analysis

### 02: Preprocessing
- Duplicate removal (keep last)
- Missing value handling:
  - Column threshold dropping
  - Refund forward-fill
  - Fines mean imputation
- Make/Model column splitting
- JSON export with clean schema

### 03: Selects and Aggregations
- Complex filtering:
  - Fine amounts
  - Refund status
  - Model lists
  - License plate lists
- Multi-level aggregations:
  - Median fines by make/model
  - Violation frequency
  - Fine amount variance
  - Top offenders analysis

### 04: Enrichment and Transformations
- Dataset expansion:
  - Random sampling (seed=21)
  - Year generation (1980-2019)
  - Surname merging
- Join operations:
  - Inner/outer/left/right
- Pivot table creation
- CSV export

### 05: Pandas Optimizations
- Performance benchmarking:
  - Iteration methods comparison
  - Indexing optimization
- Memory management:
  - Downcasting numerics
  - Categorical conversion
  - Garbage collection
- %%timeit usage
