
class Person(object):
    def __init__(self, name, designation, gender):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.personsList = []
        self.total_persons = len(self.personsList)




class Staff(Person):
    def __init__(self, staff_name, allocated_room):
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
        self.wants_livingspace = False

        if self.wants_livingspace == True:
            print ('Y')
        else:
            print ('N')
