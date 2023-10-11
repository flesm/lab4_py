from abc import ABC, abstractmethod


class PetStore:
    pass


class Animals(ABC, PetStore):
    def __init__(self, breed, cost):
        self.breed = breed
        self.cost = cost

    @abstractmethod
    def movement(self):
        pass


class Fish(Animals):
    def __init__(self, breed, cost):
        super().__init__(breed, cost)

    def movement(self):
        print("Я рыба - я плаваю.")


class Bird(Animals):
    def __init__(self, breed, cost):
        super().__init__(breed, cost)

    def movement(self):
        print("Я птушка - я лётаю.")
