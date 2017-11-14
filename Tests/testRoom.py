import unittest
from room import Room

class RoomClassTest(unittest.testcase):
    def test_room_instance(self):
        blue = Room('blue')
        self.assertIsInstance(blue, Room, msg = 'The object should be a type of Room')

    def test_create_room(self):
        blue_office = blue.create_room('Blue', 'office')
        self.assertTrue(blue_office)
        current_occupancy = len(blue.memberList)

    def test_check_occupancy(self):
        self.assertEqual((current_occupancy < max_occupancy), 'current_occupancy should be less the maximum')

        if __name__ == '__main__':
            unittest.main()
