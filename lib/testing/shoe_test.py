#!/usr/bin/env python3

import pytest
from lib.shoe import Shoe

import io
import sys


class TestShoe:
    def test_shoe_initialization(self):
        shoe = Shoe("Nike", 9.5, "Leather")
        assert shoe.brand == "Nike"
        assert shoe.size == 9.5
        assert shoe.material == "Leather"

    def test_brand_validation(self):
        with pytest.raises(ValueError):
            Shoe(123, 9.5, "Leather")  # brand is not a string

    def test_size_validation(self):
        with pytest.raises(ValueError):
            Shoe("Nike", -9.5, "Leather")  # size is negative
        with pytest.raises(ValueError):
            Shoe("Nike", "nine", "Leather")  # size is not a number

    def test_material_validation(self):
        with pytest.raises(ValueError):
            Shoe("Nike", 9.5, 123)  # material is not a string

    def test_brand_setter(self):
        shoe = Shoe("Nike", 9.5, "Leather")
        shoe.brand = "Adidas"
        assert shoe.brand == "Adidas"

        with pytest.raises(ValueError):
            shoe.brand = 123  # brand is not a string

    def test_size_setter(self):
        shoe = Shoe("Nike", 9.5, "Leather")
        shoe.size = 10.0
        assert shoe.size == 10.0

        with pytest.raises(ValueError):
            shoe.size = -10.0  # size is negative
        with pytest.raises(ValueError):
            shoe.size = "ten"  # size is not a number

    def test_material_setter(self):
        shoe = Shoe("Nike", 9.5, "Leather")
        shoe.material = "Synthetic"
        assert shoe.material == "Synthetic"

        with pytest.raises(ValueError):
            shoe.material = 123  # material is not a string

   
