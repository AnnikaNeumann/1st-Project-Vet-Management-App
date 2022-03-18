class Animal:
    def __init__(self, name, dob, breed, neutered, treatments, id = None):
        self.name = name
        self.dob = dob
        self.breed = breed
        self.neutered = neutered 
        self.treatments = treatments
        self.id = id

    def animal_has_name(self):
        return Animal


# make neutered attribute a boolean
# dob to be a string for now VARCHAR(255) in SQL


