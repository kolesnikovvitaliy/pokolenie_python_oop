''' Первый вариант решения'''
class Pet:
    pets = [] 
    def __init__(self, name):
        self.name = name  
        __class__.pets.append(self)   

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @classmethod
    def first_pet(cls):
        if cls.pets:
            return cls.pets[0]
        else:
            return None
        
    @classmethod
    def last_pet(cls):
        if cls.pets:
            return cls.pets[-1]
        else:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.pets)
''' Второй вариант решения'''    
# class Pet:
#     pets = []

#     def __init__(self, name):
#         self.name = name
#         Pet.pets.append(self)

#     @classmethod
#     def first_pet(cls):
#         return cls.pets[0] if cls.pets else None

#     @classmethod
#     def last_pet(cls):
#         return cls.pets[-1] if cls.pets else None

#     @classmethod
#     def num_of_pets(cls):
#         return len(cls.pets)