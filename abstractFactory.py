class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:

    def get_pet(self):
        """Returns a Dog object"""


    def get_food(self):
        """Returns a Dog Food object"""


class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """pet_factory is our Abstract Factory"""

    def show_pet(self):
        """Utility method to display the details of the objects returned be the DogFactory"""

        print("Our pet is '{}'".format(pet))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'".format(pet_food))
        