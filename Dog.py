class Dog():
     def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color=color
     def sit(self):
        print(self.name.title() + " is now sitting.")

     def roll_over(self):
         print(self.name.title() + " rolled over!")

     def speak(self, sound):
         print("sound of the dog",sound)
D=Dog("dog",23,"red")
D1=Dog("papi",10,"white")
