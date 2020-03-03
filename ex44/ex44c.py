#Inheritance
#Alter Before or After

# class Parent(object):

    # def altered(self):
        # print("PARENT altered()")

# class Child(Parent):

    # def altered(self):
        # print("CHILD, BEFORE PARENT altered()")
        # super(Child, self).altered()
        # print("CHILD, ARTER PARENT altered()")

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()

class Father(object):

    def altered(self):
        print("Call of altered function in Father class")

class Son(Father):

    def altered(self):
        print("Line before altered in Son class")
        super(Son, self).altered()
        print("Line after altered in Son class")

obj1 = Father()
obj2 = Son()

obj1.altered()
obj2.altered()