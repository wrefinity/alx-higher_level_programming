#!/usr/bin/python3
for x in range(97, 123):
    if x == 113 or x == 101:
        continue
    else:
        print("{:c}".format(x), end='')
