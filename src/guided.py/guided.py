# import math

# radius = 3

# print(math.pi * radius * radius)

# We'll say that a positive int divides itself
# if every digit in the number divides into the
# number evenly.
# So for example 128 divides itself
# since 1, 2, and 8 all divide into 128 evenly. 
# And we'll say that 0 does not divide into anything
# evenly, so no number with a 0 digit divides itself. 
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]

#questions:
# How big are the numbers we receive as input?
#Assumptions:
#The test has to work on all numbers
#output will be a boolean

def divides_self(num):
    #num is 10

    # if num is equal to zero
    if num == 0:
        return False
    #if length of input is 1
    if len(str(num)) == 1:
        return True

    #split input into iterable collection of integers
    #loop over collection of digits
    for digit in str(num):
        digit_int = int(digit)
        #if num is evenly divisible by current digit or current digist is 0
        if digit_int == 0 or num % digit_int != 0:
            return False

    return True


print(divides_self(0)) # false
print(divides_self(1)) #true
print(divides_self(10)) #false


print(divides_self(128)) #true
print(divides_self(12)) #true
print(divides_self(120)) #false