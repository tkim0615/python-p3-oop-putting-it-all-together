#!/usr/bin/env python3
import ipdb
class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    # ipdb.set_trace()
    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        print('size must be an integer')
    size=property(get_size, set_size)

    def cobble(self):
        print('Your shoe is as good as new!')
        self.condition = 'New'



    