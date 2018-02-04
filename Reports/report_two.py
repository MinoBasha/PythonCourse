class Human:
 
    def sayHello(self, name=None):
 
        if name is not None:
            print 'Hello ' + name
        else:
            print 'Hello '
 
# Create instance
obj = Human()
 
# Call the method
obj.sayHello()
# output : Hello
 
# Call the method with a parameter
obj.sayHello('ahmed')
# output : Hello ahmed


# Depending on the function definition, it can be called with zero, one, two or more parameters.
# Human is a class with one method sayHello(). 
# The first parameter of this method is(name) set to None, this gives us the option to call it with or without a parameter.
# An object is created based on the class, and we call its method using zero and one parameter.
