#!/usr/bin/env python3

nums = list(map(int,input("please, no but really enter some numbers :\n").split()))
# .split() allows for multiple inputs from a user
# we use the list(map(int( because we need to type cast and make it possible to iterate otherwise it is an unsupported operand
#then we are simply taking all the user input and printing the sum of it .
print(sum(nums))
