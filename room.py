from src.person import*
class Room(object):

    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type
        self.member_list = []
        self.max_occupancy = 0
        self.current_occupancy = len(self.member_list)

    def create_room(self):
        print (self.room_name, self.room_type)
        print('Room created successfully!')

    def add_member(self, new_member):
        self.member_list.append(new_member)

    def get_members(self):
        self.member_list

    def check_occupancy(self):
        if self.current_occupancy == self.max_occupancy:
            print ('This room is full to capacity..sorry')
        else:
            print ('This room still has available space!')


class Living_space(Room):
    livingspace_by_gender = {'male':[], 'female':[]}

    def __init__(self, room_name, room_gender):
        super(Living_space, self).__init__(room_name,room_gender)
        self.room_name = room_name
        self.max_occupancy = 4
        self.room_gender = room_gender
        self.wants_livingspace = False

    def allocation_by_gender(self):
        while self.current_occupancy < self.max_occupancy and self.wants_livingspace is True:
            if self.room_gender == 'female' and Person.gender == 'F':
                self.livingspace_by_gender['female'].append(Person)
            else:
                 self.livingspace_by_gender['male'].append(Person)
                 break



class Office(Room):
    def __init__(self, room_name):
        super(Office, self).__init__(room_name)
        self.room_name = room_name
        self.max_occupancy = 6
