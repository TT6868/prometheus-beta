import pytest
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.word_capitalizer import capitalize_words

def test_capitalize_words_basic():
    assert capitalize_words("hello world") == "Hello World"

def test_capitalize_words_already_capitalized():
    assert capitalize_words("Hello World") == "Hello World"

def test_capitalize_words_mixed_case():
    assert capitalize_words("hELLo wORLd") == "Hello World"

def test_capitalize_words_multiple_spaces():
    assert capitalize_words("  hello   world  ") == "Hello World"

def test_capitalize_words_empty_string():
    assert capitalize_words("") == ""

def test_capitalize_words_single_word():
    assert capitalize_words("python") == "Python"

def test_capitalize_words_invalid_input():
    with pytest.raises(TypeError):
        capitalize_words(123)
    with pytest.raises(TypeError):
        capitalize_words(None)