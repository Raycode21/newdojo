import unittest
from unittest import TestCase
from src.room import Room, Office, LivingSpace

class RoomClassTest(Testcase):
    def test_room_instance(self):
        blue = Room('blue')
        self.assertIsInstance(blue, Room, msg = 'The object should be a type of Room')
        self.current_occupancy = len(blue.self.memberList)


    def test_create_room(self):
        blue = Room('blue')
        blue_office = blue.create_room('Blue', 'office')
        self.assertTrue(blue_office)

    def test_check_occupancy(self):
        self.assertGreater (self.current_occupancy, self.max_occupancy, 'current_occupancy should be less the maximum')

class LivingSpaceClassTest(Testcase):
    def test_allocate_by_gender(self):
        self.assertEqual({self.room_gender: 'female',self.Person.gender : 'F'}, msg = 'please fill in gender')

    if __name__ == '__main__':
        unittest.main()
