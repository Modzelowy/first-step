# keyword arguments and positional arguments
# keyword arguments if comibined with positional then
# positional must come first then keyword arguments


# def test_function_positional_args(arg1, arg2, arg3):
#    print(arg1)
#    print(arg2)
#    print(arg3)
# test_function_positional_args( 1,arg3 = "hello", arg2 = 3)

# default arguments runed


# def test_func_def_val(argument = "drzewo", arg2 = 2 ):
#    print(argument)
#    print(arg2)
# test_func_def_val()

# Greeter using positional argument + 2 keywords default value same principal as the kkeyword + positional non default value must come first
# using line break to print it is weekday

# def Greeter(weekday, person="Person", greet="hello"):
#    print(f"{greet} {person}\nit is  {weekday}")
# Greeter("Wensday",greet = "Hi", person = "Mark")


# creates a tuple with all the values passed as arguments into parameter of *args this takes unlimited number of args
# This is a fine approach


# def print_all(*arg):
#    print(arg)
# print_all(1, 2 ,3 ,4 ,5 )


# we could also then iterate through the values with for loop for printing each individualy

# def print_all(*args):
#    for arg in args:
#     print(arg)
# print_all(1,2,3,4,5,6)


# keyword unpacking
# def print_more(**arguments):
#    print(arguments)
# print_more(arg1 = "chleb", arg2 = "drzewa", arg3 = 3)

# tutaj pierw zrobilem błąd nie iterując po tupli za pomocą pętli for przez co otrzymałem
# unsupported operand int + tuple

# def unlimited_sum(*args):
#    total = 0
#    for arg in args:
#        total += arg
#    return total
# print(unlimited_sum(1,2,3,4,5))

# other approach for unlimited sum much better i think czyli sum przyjął tuple bez problemu jako argument i dodał jej zawartość do siebie
# def unlimited_sum(*args):
#    sum(args)
# unlimited_sum(1,2,3,4,5)

# scope
# moge normalnie odczytać value z global scope w local scope

# zasady scope
# kazda funkcja ma wlasny local scope i kazdy local scope jest oddzielny
# nie moge globali  zmieniac w localu dopoki nie zrobię czegoś
# do tego sluzy global i return
# global nie powinno się używać
# powinienem używać return


# random_var = 13
# def test_func():
#    print(random_var)
# test_func()

####
# a = 12
# przyklad uzycia return w celu uzyskania zmiany value a


# def test_scope():
#    print(a + 2)
#    return a
# test_scope()

# przyklad uzycia argumentu aby przy wywolywaniu uzyc globalnego vara do zmiany jego value
# def test_scope_2(a):
#    print(a +2)
# test_scope_2(a)
####

# tutaj wykorzystuje global zeby zupdatowac po kalkulacji value has_calculated na true
# uzywam tego ze moge accesnoac globalke w localku i mnoze razy argument zapisujac do nowej zmiennej
# printuje ów var
# do czego mialbym uzyc return???? jak dokladnie to dziala?
# multipler = 13
# has_calculated = False

# def multiply_calculator(number: int) -> int:
# global has_calculated
# calculation =   multipler * number
# has_calculated = True
# print(calculation)
# multiply_calculator(3)

# lambda
# lambda var : kod
# lambda to jednoliniowa prosta funkcja w jednej linijce kodu
# returnuje automatycznie
# podajesz argument dla którego ma być wywołana na końcu i żeby ją właściwie wywołać musisz całą funkcję lambda również zawrzeć w nawiasie
# to jest ternarny operatation
# value_if_true if condition else value_if_false
# (lambda varek: print("hello") if varek > 5 else print("nonono")) (3)

# ćwieczenia na funkcjach pare prostych ćwiczeń stworzonych przez czat gpt
# 1 ćwiczenie
# Napisz funkcję, która przyjmuje dwa argumenty, a i b, i zwraca ich sumę. Wywołaj funkcję z argumentami 2 i 3 i wyświetl wynik.
# def kalku(a,b):
#    result = a + b
#    return result
# print(kalku(5,3))

# 2 cwieczenie
# Napisz funkcję, która przyjmuje argument tekstowy i zwraca jego długość. Wywołaj funkcję z tekstem "Hello world!" i wyświetl wynik.

# def length_of_word(the_string: str) -> int:
#    result = len(the_string)
#    return result
# print(length_of_word("Hello world!"))

# 3 cwiczenie
# Napisz funkcję, która przyjmuje listę liczb i zwraca ich sumę. Wywołaj funkcję z listą [1, 2, 3, 4] i wyświetl wynik


# def list_sum(listeczka: list) -> int:
#    result = sum(listeczka)
#    return result
# print(list_sum([1,2,3,4]))

# Napisz funkcję, która przyjmuje argument liczbowy i zwraca True, jeśli liczba jest parzysta,
# a False w przeciwnym przypadku. Wywołaj funkcję z liczbą 6 i wyświetl wynik
# def check_if_parzysta(arg:int) -> bool:
#    return True if arg % 2 == 0 else False

# print(check_if_parzysta(3))

# Napisz funkcję, która przyjmuje argumenty a, b i c i zwraca wynik równania kwadratowego ax ^ 2 + bx + c.
# Wywołaj funkcję z argumentami a = 2, b = 4, c = 2 i wyświetl wynik.
# import math
# def rownianie_kwadratowe(a,b,c : int) -> float:

#   delta = (b ** 2) - (4 * a * c)
#    x_1 = (-b - math.sqrt(delta) ) / (2 * a)
#    x_2 = (-b + math.sqrt(delta)) / (2 * a)
#    return x_1, x_2
# print(rownianie_kwadratowe(2,4,2))

# Napisz funkcję, która przyjmuje argument tekstowy i zwraca liczbę wystąpień litery "a" w tym tekście.
# Wywołaj funkcję z tekstem "abrakadabra" i wyświetl wynik.
# def liczba_wystapien_liter(wyraz : str) -> int:
#   counter = 0

#  for a in wyraz:
#       if a == "a":
#        counter += 1
#   result = counter
#   return result
# print(liczba_wystapien_liter("abrakadabra"))

# Napisz funkcję, która przyjmuje dwie listy i zwraca nową listę zawierającą elementy obu list.
# # Wywołaj funkcję z listami[1, 2, 3] i[4, 5, 6] i wyświetl wynik.
# def list_function(list_1, list_2 : list) -> list:
# merged_list = list_1 + list_2
# return merged_list
# print(list_function([1,2,3], [4,5,6]))

# Napisz funkcję, która przyjmuje argument liczbowy i zwraca True, jeśli liczba jest parzysta,
# a False w przeciwnym przypadku. Wywołaj funkcję z liczbą 6 i wyświetl wynik


# def test(liczba: int) -> bool:
#     if liczba % 2 == 0:
#         result = True

#     else:
#         result = False
#     print(result)


# test(3)


# def parzysta(num):
#     return num % 2 == 0


# print(parzysta(3))
# Napisz funkcję, która przyjmuje argument tekstowy i zwraca liczbę wystąpień litery "a" w tym tekście.
# Wywołaj funkcję z tekstem "abrakadabra" i wyświetl wynik.
# def test(wyraz: str) -> int:
#     counter = 0
#     for a in wyraz:
#         if a == "a":
#             counter += 1
#     print(counter)


# test("abrakadabraaaa")
