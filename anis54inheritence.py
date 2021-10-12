# Inheritance
## phone we can call super class, parent class, base class.
### samsung we can call sub class, child class, derived class.

class phone ():
    def call (self):
        print("You can call.")
    def message (self):
        print("You can message.")

class samsung (phone):           ## Here "phone" is super class and "samsung" is sub class.
    def photo (self):
        print("You can take photo.")


a = samsung()
a.photo()
a.call()
a.message()