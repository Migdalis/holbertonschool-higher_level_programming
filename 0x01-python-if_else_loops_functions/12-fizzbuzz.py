#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        mult_t = i % 3
        mult_f = i % 5
        
        if ((mult_t == 0) and (mult_f == 0)):
            print("FizzBuzz ", end="")
        elif (mult_t == 0):
            print("Fizz ", end="")
        elif (mult_f == 0):
            print("Buzz ", end="")
        else:
            print("{:d} ".format(i), end="")
