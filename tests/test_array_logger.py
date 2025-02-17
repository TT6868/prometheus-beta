import pytest
from src.array_logger import log_array_as_table

def test_flat_array_logging():
    arr = [1, 2, 3, 4, 5]
    expected = (
        "Index | Value\n"
        "---------------\n"
        "0     | 1     \n"
        "1     | 2     \n"
        "2     | 3     \n"
        "3     | 4     \n"
        "4     | 5     "
    )
    assert log_array_as_table(arr).replace("\n", "\\n") == expected.replace("\n", "\\n")

def test_nested_array_logging():
    arr = [[1, 'a'], [2, 'b'], [3, 'c']]
    expected = (
        "0 | a\n"
        "------------\n"
        "1 | a\n"
        "2 | b\n"
        "3 | c"
    )
    assert log_array_as_table(arr, headers=[0, 1]).replace("\n", "\\n") == expected.replace("\n", "\\n")

def test_custom_headers():
    arr = [1, 2, 3, 4, 5]
    expected = (
        "Number | Score\n"
        "------------------\n"
        "0      | 1     \n"
        "1      | 2     \n"
        "2      | 3     \n"
        "3      | 4     \n"
        "4      | 5     "
    )
    assert log_array_as_table(arr, headers=['Number', 'Score']).replace("\n", "\\n") == expected.replace("\n", "\\n")

def test_empty_array():
    arr = []
    assert log_array_as_table(arr) == "Empty array"

def test_invalid_input():
    with pytest.raises(TypeError):
        log_array_as_table("not a list")

def test_mismatched_headers():
    with pytest.raises(ValueError):
        log_array_as_table([1, 2, 3], headers=['Too', 'Many', 'Headers'])