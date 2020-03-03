#Inheritence
#Override Explicity

# class Parent(object):
    
    # def override(self):
        # print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# class Dad(object):

    # def override(self):
        # print("Method called from Dad class")

# class Son(Dad):
    
    # def override(self):
        # print("Method called from Son class")

# obj1 = Dad()
# obj2 = Son()

# obj1.override()
# obj2.override()