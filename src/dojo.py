from abc import ABCmeta, abstractMethod
__metaclass__ = ABCmeta

@abstractMethod
def something(self):
        pass
        
class Dojo(object):
    
    def __init__(self, name, occupancy):
        self.name = name
        self.occupancy = 0
        
    
        

