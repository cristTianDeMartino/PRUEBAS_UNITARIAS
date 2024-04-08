def sum(x,  y):
    return x + y 


def is_greater_than(number_1, number_2):
    return number_1 > number_2  

def  login(username, password):
    if  ((username == "alumnouady") and  (password == "uady1234")):
         return True
    else:
        return False
def is_odd(num):
    # returns true if number is odd
    return num % 2 == 1

def is_even(num):
    # returns true if number is even
    return is_odd(num) == False
    