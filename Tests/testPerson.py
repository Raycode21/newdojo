import unittest
from unittest import TestCase
from src.room import Person, Fellow, Staff

class PersonClassTest(Testcase):
    def test_person_instance(self):
        rachel = Person('Rachel')
        self.assertIsInstance(rachel, Person, msg = 'object should be a type of Person')

class StaffClassTest(Testcase):
    def test_allocated_room(self):
        self.assertEqual(self.allocated_room, 'office', msg = 'Staff can only be allocated to office')
class FellowClasstest(Testcase):
    def test_wants_room(self):
        rachel = Person('Rachel')
        self.assertTrue(rachel.wants_room, msg = 'This person must be assigned a room if unless they are staff')
    if __name__ == '__main__':
        unittest.main()
