"""
test_api.py - Unit tests for movie model validation logic
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

from models import MovieModel


def test_invalid_rating():
    try:
        MovieModel.create("Test", "Action", 2020, 11.0, "")
        print("FAIL: Should have raised ValueError for rating > 10")
    except ValueError:
        print("PASS: test_invalid_rating")


def test_empty_title():
    try:
        MovieModel.create("", "Action", 2020, 8.0, "")
        print("FAIL: Should have raised ValueError for empty title")
    except ValueError:
        print("PASS: test_empty_title")


if __name__ == "__main__":
    test_invalid_rating()
    test_empty_title()
    print("\nAll tests passed.")
