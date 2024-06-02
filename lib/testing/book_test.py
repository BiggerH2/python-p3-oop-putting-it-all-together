#!/usr/bin/env python3
import pytest
from lib.book import Book

import io
import sys


class TestBook:
    def test_book_initialization(self):
        book = Book("1984", "George Orwell", 328)
        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.page_count == 328

    def test_title_validation(self):
        with pytest.raises(ValueError):
            Book(1984, "George Orwell", 328)  # title is not a string

    def test_author_validation(self):
        with pytest.raises(ValueError):
            Book("1984", 1984, 328)  # author is not a string

    def test_page_count_validation(self):
        with pytest.raises(ValueError):
            Book("1984", "George Orwell", -328)  # page_count is negative
        with pytest.raises(ValueError):
            Book("1984", "George Orwell", "three hundred")  # page_count is not an integer

    def test_title_setter(self):
        book = Book("1984", "George Orwell", 328)
        book.title = "Animal Farm"
        assert book.title == "Animal Farm"

        with pytest.raises(ValueError):
            book.title = 123  # title is not a string

    def test_author_setter(self):
        book = Book("1984", "George Orwell", 328)
        book.author = "Eric Blair"
        assert book.author == "Eric Blair"

        with pytest.raises(ValueError):
            book.author = 123  # author is not a string

    def test_page_count_setter(self):
        book = Book("1984", "George Orwell", 328)
        book.page_count = 112
        assert book.page_count == 112

        with pytest.raises(ValueError):
            book.page_count = -112  # page_count is negative
        with pytest.raises(ValueError):
            book.page_count = "one hundred twelve"  # page_count is not an integer
