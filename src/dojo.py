from newdojo.src.person import Person
from newdojo.src.room import Room
class Dojo(object):
    available_rooms = {'offices':'', 'living_spaces':''}

    def __init__(self):

        self.all_rooms = []
        self.total_rooms = len(self.all_rooms)
        self.current_occupancy = 0
        self.allocated_rooms = []
        self.unallocated_rooms = []
        self.max_occupancy = 50

    def allocate_person(self):
        if Person.designation == 'fellow' and Person.wants_livingspace == True:
            (self.available_rooms['living_spaces'])[0].append(Person)
        Person.allocated_persons.append(Person)


    def number_of_available_rooms(self):
        if self.current_occupancy < self.max_occupancy:
           len(self.available_rooms)

    def add_room(self, new_room):
        self.all_rooms.append(new_room)

    def allocate_room(self, wants_livingspace = False):
        if Person.designation == 'fellow' and Person.wants_livingspace is True:
            self.allocate_person()
            Person.allocated_persons.append(Person)
