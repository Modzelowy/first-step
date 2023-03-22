# inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
# inventory_numbers = [43, 12,95, 421,23,43]

# exercise
# combine zip and enumerate to get string
# "Screws [id : 0] quantity - 43"

# for index,name_and_index_tuple in enumerate(zip(inventory_names,inventory_numbers)):

#       print(f"{name_and_index_tuple[0]} [id : {index}] quantity - {name_and_index_tuple[1]}")

# List comprehension
# lista_comp = [num for num in range(0,100)]
# print(lista_comp)

# list comprehension with ternary operation
# warunek na końcu jeśli chcesz samego ifa
# warunek na początku jeśli ma być else
# list_comp_1 = [num if num > 5 else 0 for num in range(0, 100) ]
# print(list_comp_1)

# inventory_names = ["Screws", "Wheels", "Metal parts", "Rubber bits", "Screwdrivers", "Wood"]
# inventory_numbers = [43, 12,95, 421,23,43]
# replenish_list = [ (name, number) for name, number in list(zip(inventory_names,inventory_numbers)) if number <25]

# combined_comprihension = [[x for x in range(5)] for y in  range (2)]
# print(combined_comprihension)

# create chess board by using list combined list comprehension
# trudne i irytujace
# list_for_exercise = [
#    [(num_pos, char_pos) for num_pos in range(1, 9)] for char_pos in "ABCDEFGH"[::-1]
# ]#
# for row in list_for_exercise:
#    print(row)

# ternary operation
# value_if_true if condition else value_if_false
# list comp
# new_list = [expression for item in old_list if condition]
# list comp + ternaru
# new_list = [expression1 if condition else expression2 for item in old_list if condition2]

# Utwórz listę liczb od 1 do 10. Następnie utwórz nową listę zawierającą tylko parzyste liczby z pierwszej listy.
# Podpowiedź: użyj List Comprehension z warunkiem if, który sprawdza czy liczba jest parzysta.
# list_1_to_10 = [x for x in range(1, 11)]
# print(list_1_to_10)
# list_1_to_10_only_even = [b for b in list_1_to_10 if b % 2 == 0]
# print(list_1_to_10_only_even)

# Utwórz listę imion: "Anna", "Bob", "Cathy", "David". Następnie utwórz nową listę zawierającą tylko imiona z pierwszej listy, które zaczynają się od litery "A".
# Podpowiedź: użyj List Comprehension z warunkiem if, który sprawdza czy imię zaczyna się
# list_of_names = ["Anna", "Bob ", "Cathy", "David", "Andrew"]

# list_of_names_but_starts_with_A = [name for name in list_of_names if name[0][0] == "A"]

# print(list_of_names_but_starts_with_A)

#    Stwórz listę zawierającą liczby od 1 do 20.
#    Wykorzystaj List Comprehension do wygenerowania listy.
# list_num = [x for x in range(1, 21)]
# print(list_num)

#    Stwórz listę zawierającą kwadraty liczb od 1 do 10.
#   Wykorzystaj List Comprehension i operator potęgowania.
# list_num_before = [liczby for liczby in range(1, 11)]
# list_num_after = [liczby**2 for liczby in list_num_before]
# print(list_num_after)
# Stwórz listę zawierającą wartości True lub False w zależności od tego, czy liczba w liście z punktu 1 jest większa niż 10.
# list_num = [x for x in range(1, 21)]
# ista_boli = [True if x > 10 else False for x in list_num]
# p#rint(lista_boli)


# lista, na której będziemy pracować
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# import math

#    Stwórz listę, w której każdy element będzie pomnożony przez 2, jeśli jest on podzielny przez 2, lub podzielony przez 3, jeśli nie jest podzielny przez 2.
#    Stwórz listę, która zawiera liczby z listy nums, pomnożone przez 10, jeśli są one większe niż 5, lub podzielone przez 2, jeśli są mniejsze lub równe 5.
#    Stwórz listę, która zawiera wartości logiczne True, jeśli dany element z listy nums jest większy niż 5, lub wartości False, jeśli jest mniejszy lub równy 5.
#    Stwórz listę, w której każdy element będzie równy pierwiastkowi kwadratowemu z odpowiadającego mu elementu z listy nums, jeśli jest on większy niż 5, lub zero, jeśli jest mniejszy lub równy 5.
#    Wskazówka: do obliczenia pierwiastka kwadratowego można użyć funkcji sqrt() z modułu math. Przykład użycia: import math; math.sqrt(4).
# zadanie_1 = [x * 2 if x % 2 == 0 else x / 3 for x in nums]
# zadanie_2 = [x * 10 if x > 5 else x / 2 for x in nums]
# zadanie_3 = [True if x > 5 else False for x in nums]
# zadanie_4 = [math.sqrt(x) if x > 5 else 0 for x in nums]
# print(zadanie_4)
#   Stwórz listę, która zawiera liczby z listy nums, pomnożone przez 2, jeśli są one podzielne przez 2 i większe niż 4,
# lub podzielone przez 3, jeśli są mniejsze lub równe 4.
#   Stwórz listę, która zawiera liczby z listy nums, podzielone przez 2 i pomnożone przez 10,
# jeśli są one większe niż 5 i nieparzyste, lub podzielone przez 3, jeśli są mniejsze lub równe 5 lub parzyste.

# Wskazówka: do sprawdzenia, czy liczba jest parzysta, można użyć operatora modulo %. Przykład użycia: 4 % 2 == 0.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# zadanie_1_1 = [x * 2 if x % 2 == 0 and x > 4 else x / 3 for x in nums]
# zadanie_1_2 = [x / 2 * 10 if x > 5 and x % 2 == 0 else x / 3 for x in nums]

# set comprihension
# random_set = {num for num in range(0, 11)}
# print(random_set)

# dict comprehension
# random_dict = {num: num for num in range(0, 11)}
# random_dict = {num: num * 2 for num in range(0, 11)}
# print(random_dict)

# tuple comprehension
# random_tuple = tuple(x for x in range(0, 11))
# print(random_tuple)

# exercise
# create a dictionary with Keys ["A", "B", "C", "D", "E"]
# each  key should have a list as value with values [1,2,3,4,5]

# list_for_exec = ["A", "B", "C", "D", "E"]
# list_for_exec_2 = [[1, 2, 3, 4, 5]]
# exec_dict = {key: value for key in list_for_exec for value in list_for_exec_2}
# print(exec_dict)

# inaczej
# exec_dict = {key: value for key in "ABCDE" for value in [[1, 2, 3, 4, 5]]}
# print(exec_dict)

# function as argument in sorted
# list_1 = [4, 2, 3, 1, 5]
# print(sorted(list_1))
# print(sorted(list_1, reverse = True))

# list2 = [("a", 3), ("b", 10), ("c", 6), ("d", 5)]


# def func_for_sort(item):
#    return item[1]


# print(sorted(list2, key=func_for_sort))
# print(sorted(list2, key=lambda item: item[1]))

# exercise
# inventory_names = [
#    "Screws",
#    "Wheels",
#   "Metal parts",
#    "Rubber bits",
#    "Screwdrivers",
#   "Wood",
# ]
# inventory_numbers = [43, 12, 95, 421, 23, 43]
# combined_list = list(zip(inventory_names, inventory_numbers))
# 1. sort this list by inventory numbers
# print(sorted(combined_list, key=lambda item: item[1]))
# 2. sorte this list by length of the inventory name
# print(sorted(combined_list, key=lambda item: len(item[0])))
# ^ nie wiem co tu robię ale działa XD

# list1 = [1, 2, 3, 4, 5]
# function as argument for map and filter:
# map - changes values with a function in iterable
# print(list(map(lambda power: power**2, list1)))

# filter a list from a values from the condition
# print(list(filter(lambda filt: filt < 4, list1)))

# execrise recreate map and filter using list comprehension
# list_for_exec_lmao1 = [num for num in list1 if num < 4]
# print(list_for_exec_lmao1)

# list_for_exec_lmao2 = [num**2 for num in list1]
# print(list_for_exec_lmao2)


# file handling
# open and close manually / not used often
# file = open("text.txt")
# print(list(file))
# file.close()

# open and close automatically
# with open("text.txt") as file:
#    print(file.read())

# write a file open("nazwa pliku", argument w stringu "a" append "w" zalozy nowy plik)
# with open("text.txt", "a") as file:
#    file.write("\nwrite some more")

# exercise
# create a new file with tree in it
# with open("drzewo.txt", "w") as drzewo:
#    drzewo.write("   X   ")
#    drzewo.write("\n  XXX  ")
#    drzewo.write("\n XXXXX")
#    drzewo.write("\nXXXXXXX")
#    drzewo.write("\n   X")
#    drzewo.write("\n   X")


# delete shit
# del thing
# a = 1
# del a
# print(a)

# remove items from the list
# a = [1, 2, 3]
# del a[1]
# print(a)

# remove item by value
# a.remove(value)
# a.pop(index) return a -> then remove

# clear entire list
# a.clear()
