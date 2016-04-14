#!/usr/bin/env python

# This is a simple brute force proof of the "Birthday paradox"
# https://en.wikipedia.org/wiki/Birthday_problem
import random

number_of_people = 23
iterations = 1000

print("Running the Birthday paradox")
print("N=%d".format(number_of_people))
PASS = 0.0
for _ in xrange(iterations):
    birthday_list = set()
    for _ in xrange(number_of_people):
        bday = random.randint(1,365)
        if bday in birthday_list:
            PASS += 1
            break
        else:
            birthday_list.add(bday)

print("p(N): {0:0.3}".format(PASS/iterations))
