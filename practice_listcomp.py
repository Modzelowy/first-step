# Find all numbers from 1-1000 that are divisiable by 7
# x = [num for num in range(1, 1001) if num % 7 == 0]
# print(x)

# find all numbers from 1-1000 that have "3 " in them
# x = [num for num in range(1, 1001) if "3" in str(num)]
# print(x)

# Count the number of spaces in a string
# string = "kurwa do chuja pana pierdole to wszystko"
# spaces = [space for space in string if space == " "]
# print(len(spaces))


# Create a list of all the consonants in the string
# stringer = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"
# bowels = "bcdfghjklmnpqrstvwxyz"
# list_for_counting_bowels = [
#     letter for letter in stringer for bowel in bowels if letter == bowel
# ]
# print(len(list_for_counting_bowels))


# Get the index and the value as a tuple for items in the list
# lista  ["hi", 4, 8.99, "apple", ("t,b", "n")]
# Result would look like (index, value), (index, value)
# listaaa = [(idx, value) for idx, value in enumerate(lista)]
# print(listaaa)

# Find the common numbers in two lists (without using a tuple or set)
# list_a = [
#     1,
#     2,
#     3,
#     4,
# ]
# list_b = [2, 3, 4, 5]
# wspolne = [common for common in list_a if common in list_b]
# print(wspolne)

# Get only the numbers in a sentence like ‘
# stringer = (
#     "In 1984 there were 13 instances of a protest with over 1000 people attending"
# )
# lista = [int(number) for number in stringer.split() if number.isdigit()]
# print(lista)

# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, and the word ‘odd’
# if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
# lista = ["ODD" if num % 2 else "EVEN" for num in range(20)]
# print(lista)

# listeczka = [[n for n in range(1, 4)] for n in range(1, 4)]

# lista = [[j, j, j] for j in range(1, 4)]
# print(lista)

# Produce a list of tuples consisting of only the matching numbers in the
# se lists Result would look like (4,4), (12,12)

# list_a = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     6,
#     7,
#     8,
#     9,
# ]
# list_b = [
#     2,
#     7,
#     1,
#     12,
# ]

# wspolne_tuple = [(common, common) for common in list_a if common in list_b]
# print(wspolne_tuple)

# Find all of the words in a string that are less than 4 letters
# stringer = "i choćbym szedł doliną cieni zła się nie uleknę bo ty jesteś przy mnie"
# modified_string = stringer.split()
# print(modified_string)
# lista_slow = [word for word in modified_string if len(word) < 4]
# print(lista_slow)
# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)

# lista = [
#     num
#     for num in range(1, 1001)
#     if True in [True for x in range(2, 10) if num % x == 0]
# ]
# print(lista)

# for x in range(1, 1001):
#     for div in range(2, 10):
#         if x % div == 0:
#             print(x)
# def check_if_divisable(n):
#     for i in range(2, 10):
#         if n % i == 0:
#             return True
#     return False


# check_if_divisable(13)

# /a pozniej zró tak:

# -lista 0-1000 podzielnych przez 2
# - lista 0-1000, które są podzielne przez którąkolwiek 2-9 (masz do tego gotową funkcję

# robie_to_szesnanty_raz = [i for i in range(1, 1001) if i % 2 == 0]
# print(robie_to_szesnanty_raz)

# lista = [n for n in range(1, 1001) if check_if_divisable(n)]
# print(lista)


# n = 9
# divisors = [n % number == 0 for number in range(2, 10)]
# print(any(divisors))

# -lista 0-1000 podzielnych przez 2
# - lista 0-1000, które są podzielne przez którąkolwiek 2-9 (masz do tego gotową funkcję
# divisible_nums = [
#     num for num in range(0, 1001) if any(num % divisor == 0 for divisor in range(2, 10))
# ]
# print(divisible_nums)
