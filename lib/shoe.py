#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, material):
        self.brand = brand
        self.size = size
        self.material = material

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str):
            raise ValueError("Brand must be a string")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Size must be a positive number")
        self._size = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if not isinstance(value, str):
            raise ValueError("Material must be a string")
        self._material = value
