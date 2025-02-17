# Day of Week Utility

A simple Python utility to get the day of the week for a given date.

## Features

- Convert dates to day names
- Support for string and datetime inputs
- Robust error handling

## Usage

```python
from src.day_of_week import get_day_of_week

# Using a date string
print(get_day_of_week('2023-06-21'))  # Outputs: Wednesday

# Using a datetime object
from datetime import datetime
date = datetime(2023, 12, 25)
print(get_day_of_week(date))  # Outputs: Monday
```

## Running Tests

Use pytest to run the tests:

```
pytest tests/
```