from person import Person
from room import Room
class Dojo(object):
    available_rooms = {'offices':'', 'living_spaces':''}

    def __init__(self):

        self.all_rooms = []
        self.total_rooms = len(self.all_rooms)
        self.current_occupancy = 0
        self.allocated_rooms = []
        self.unallocated_rooms = []
        self.max_occupancy = 50


    def number_of_available_rooms(self):
        if self.current_occupancy < self.max_occupancy:
           len(self.available_rooms)

    def create_room(self):
        new_room = (Room.room_name, Room.room_type)
        print (new_room)

    def add_room(self):
        new_room = (Room.room_name, Room.room_type)
        self.all_rooms.append(new_room)

    def allocate_room(self, room, wants_livingspace = False):
        self.room = room
        if Person== 'fellow' and Person.wants_livingspace == True:
            Person.allocate_person()
            Person.allocated_persons.append(Person)
