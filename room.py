from newdojo.src.person import Person
class Room(object):


    def __init__(self,room_name, room_type, room_gender):
        self.room_name = room_name
        self.room_type = room_type
        self.room_gender = room_gender
        self.person_list = []
        self.max_occupancy = 0
        self.current_occupancy = len(self.person_list)
        self.livingspace_by_gender = {'male':[], 'female':[]}


    def allocate_by_gender(self):
        while self.current_occupancy < self.max_occupancy and Person.wants_livingspace is True:
            if self.room_gender == 'female' and Person.gender == 'F':
                self.livingspace_by_gender['female'].append(Person)
            else:
                self.livingspace_by_gender['male'].append(Person)
            break




    def create_room(self):
        new_room = (self.room_name, self.room_type)
        print new_room
        print'Room created successfully!'

    def is_full(self, new_person):

        if self.current_occupancy == self.max_occupancy:
            print 'You cannot add new members to this room!'
            Person.unallocated_persons.append(new_person)
        else:
            Person.allocated_persons.append(new_person)


    def get_all_persons(self):
        self.person_list

    def check_occupancy(self):

        if self.current_occupancy == self.max_occupancy:
            print 'This room is full to capacity..sorry'
        else:
            print 'This room still has available space!'


class Living_space(Room):
    def __init__(self, room_name, room_gender):
        super(Living_space, self).__init__(room_name, room_gender)
        self.room_name = room_name
        self.max_occupancy = 4


    def check_person_designation(self):
        if Person.designation == 'staff':
            print'only fellows are assigned livingspace'
        else:
            input('does this person want accomodation?')

class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.room_name = room_name
        self.max_occupancy = 6
        self.office_members = []
