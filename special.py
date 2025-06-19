class myClass:
    __privateVar = 27


    def __privMeth(self):
        print("I am indside my class")

    def hello(self):
        print("Private Variuble value:",myClass)

foo = myClass()
foo.hello()
foo.__privMeth # This will raise an AttributeError