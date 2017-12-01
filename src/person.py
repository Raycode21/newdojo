from newdojo.src.room import Room
class Person(object):
    wants_livingspace = False
    allocated_persons = []
    unallocated_persons = []
    designation = 'staff'

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.persons_list = []
        self.total_persons = len(self.persons_list)


    def allocate_person(self):
        if self.designation == 'fellow' and self.wants_livingspace == True:
            Living_space(Room).allocate_by_gender()


class Staff(Person):
    def __init__(self, staff_name):
        super(Staff,self).__init__(staff_name)
        self.staff_name = self.name
        self.allocated_room = 'office'
        self.staffList = []

    def staff_total(self):
        self.staffList


class Fellow(Person):
    def __init__(self, fellow_name):
        super(Fellow, self).__init__(fellow_name)
        self.fellow_name = self.name

        if self.wants_livingspace == True:
            print ('Y')
        else:
            print ('N')
