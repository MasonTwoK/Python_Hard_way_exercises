#Exercice 44 Inheritance

#Implicit Inheritance
class Parent(object):

    def implicit(self):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
