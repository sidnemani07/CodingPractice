from collections import deque

class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0

    def enqueue(self, animal, type):
        if type == 'dog':
            self.dogs.append((self.order, animal))
        elif type == 'cat':
            self.cats.append((self.order, animal))
        self.order += 1

    def dequeueAny(self):
        if not self.dogs and not self.cats:
            return None
        if not self.dogs:
            return self.cats.popleft()[1]
        if not self.cats:
            return self.dogs.popleft()[1]
        if self.dogs[0][0] < self.cats[0][0]:
            return self.dogs.popleft()[1]
        else:
            return self.cats.popleft()[1]

    def dequeueDog(self):
        return self.dogs.popleft()[1] if self.dogs else None

    def dequeueCat(self):
        return self.cats.popleft()[1] if self.cats else None

# Example usage:
shelter = AnimalShelter()
shelter.enqueue("Dog1", "dog")
shelter.enqueue("Cat1", "cat")
shelter.enqueue("Dog2", "dog")
print(shelter.dequeueAny())  # returns Dog1
print(shelter.dequeueDog())  # returns Dog2
print(shelter.dequeueCat())  # returns Cat1
