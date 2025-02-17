import pytest
from datetime import datetime
from src.day_of_week import get_day_of_week

def test_get_day_of_week_string_input():
    assert get_day_of_week('2023-06-21') == 'Wednesday'
    assert get_day_of_week('2023-12-25') == 'Monday'

def test_get_day_of_week_datetime_input():
    date_obj = datetime(2023, 6, 21)
    assert get_day_of_week(date_obj) == 'Wednesday'

def test_get_day_of_week_invalid_string_format():
    with pytest.raises(ValueError, match="Invalid date format"):
        get_day_of_week('21-06-2023')  # wrong format
        get_day_of_week('2023/06/21')  # wrong format

def test_get_day_of_week_invalid_input():
    with pytest.raises(ValueError, match="Input must be a date string or datetime object"):
        get_day_of_week(12345)  # invalid input type
        get_day_of_week(None)   # invalid input type