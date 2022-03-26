import unittest
from modules.owner import Owner

class TestOwner(unittest.TestCase):

    def setUp(self):
        self.owner_1 = Owner("Karin", "Kaefer", "0123456778")
        self.owner_2 = Owner("Alexis", "Neumann", "07754332345")

    def test_owner_has_number(self):
        self.assertEqual("0123456778", self.owner_1)

    # def owner_has_name(self):
    #     self.assertEqual("Fleming", self.owner_2)


