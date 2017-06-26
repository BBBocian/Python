#Write a function to compute 5/0 and use try/except to catch the exceptions.

def dziel():
    return 5/0

try:
    dziel()
except ZeroDivisionError:
    print("Nie dzieli sie przez zero")


#Define a custom exception class which takes a string message as attribute.

class Excep(Exception):

    def __init__(self, message):
        self.message = message

    
