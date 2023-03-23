"""
    Given an integer,

, perform the following conditional actions:

    If 

is odd, print Weird
If
is even and in the inclusive range of to
, print Not Weird
If
is even and in the inclusive range of to
, print Weird
If
is even and greater than , print Not Weird
    """

n = 2
if n in range(6, 21) and n % 2 == 0:
    print("Weird")
if n > 20 and n % 2 == 0:
    print("Not Weird")
if n % 2 != 0:
    print("Weird")
if n in range(2, 6) and n % 2 == 0:
    print("Not Weird")
if n % 2 == 0:
    print("Not Weird")
