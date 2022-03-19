import unittest
from modules.animal import Animal
from modules.owner import Owner
from modules.vet import Vet

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal("Elliot", "11092011", "Tabby_cat", "Flea and worm treatment")

    def test_animal_has_name(self):
        

