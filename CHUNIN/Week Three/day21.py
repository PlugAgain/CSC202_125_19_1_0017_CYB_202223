#writing my day 21 code below here

#Class Inheritance
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

class Whale(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this underwater")

    def swim(self):
        print("Propelling through water")

nemo = Whale()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)