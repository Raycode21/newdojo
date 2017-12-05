
import unittest
from unittest import TestCase
from newdojo.src.person import Person, Fellow, Staff

class PersonClassTest(TestCase):
        def setup(self):
            self.person = Person(name ='Charles Darwin', designation = 'staff')

        def test_person_instance(self):
            Charles = Person('Charles Darwin')
            self.assertIsInstance(Charles, Person, msg = 'object should be a type of Person')

class StaffClassTest(TestCase):
    def test_allocated_room(self):
        self.allocated_room = 'office'
        self.assertEqual(self.allocated_room, 'office', msg = 'Staff can only be allocated to office')

class FellowClasstest(TestCase):
    def test_wants_room(self):
        rachel = Person('Rachel')
        self.assertTrue(rachel.wants_room, msg = 'This person must be assigned a room if unless they are staff')

    if __name__ == '__main__':
        unittest.main()
