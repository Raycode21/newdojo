
import os
from unittest import TestCase
from src.dojo import*

def setUp(self):
    self.dojo = Dojo()

class TestCreateRoom(TestCase):
    def test_create_room_successfully(self):
        dojo = Dojo('blue')
        initial_room_count = len(dojo.all_rooms)
        blue_office = dojo.create_room('Blue', 'office')
        self.assertTrue(dojo_office)
        new_room_count = len(dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_available_rooms(self):
        available = (self.current_occupancy < self.max_occupancy)
        self.assertEqual(dojo.available_rooms(), available)

    def test_similar_room_names(self):
        new_room1 = create_room('blue', 'living_space')
        new_room2 = create_room('blue', 'living_space')
        error = 'Please select another room name that one already exists'
        new_room2 = (error, new_room2)

    def test_create_room(self):
        dojo_office = dojo.create_room('Blue', 'office')
        self.assertTrue(dojo_office)


    def test_add_room(self):
        self.assertTrue(len(self.total_rooms)+1)
    if __name__ == '__main__':
        unittest.main()
