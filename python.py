#
# to_go = 10000

# while True:
#    user_input = input('ile czasu poswieciles?')
#    try:
#        decrease_hours = int(user_input)
#        if decrease_hours < 0:
#            raise ValueError
#       to_go -= decrease_hours
#       print(to_go, 'pozostalo')
#   except ValueError:
#      print('no chyba nie cofasz sie w rozwoju')

#


# test_variable_1 = "x"
# test_variable_2 = "y"
# greet_hobby_string = f"hello my name is {test_variable_1} \nand my hobby is {test_variable_2}"
# print(greet_hobby_string)

# exercise_list = ['first entry', [123, 456, [0, 'Hello:)'] ], 'bye']
# print(exercise_list[1][2][1])


# print('hello world')
# Metody czyli zmienianie value przy return
# jakis_tam_var_1 = 'JOhn SmiThXX'
# print(jakis_tam_var_1.strip('X').title())

# SLicing
# test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# test = test_list[-3:-10:-2]
# print(test)

# value_1 = 10
# value_2 = 'test'
# value_1, value_2 = (value_2, value_1)
# print(value_1,value_2)

# test_list = [1, 2, 3, 4]
# print(type(test_list))
# test_list = str(test_list)
# print(type(test_list))
# new_obj = test_list.strip('[').strip(']').replace(',', '')
# print(new_obj)
# print(new_obj)
lista = ["A", "B", "C", "D"]
print(list(str(lista)))


# test_dictionary = {"A" : "B", "C" : "D" }
# a = test_dictionary.update({"E" : "F"})
# print(test_dictionary)
# print(a)

# my_set = {1, 2, 3, 4, 5}
# my_list_from_set = list(my_set)
# print(my_list_from_set[0])


# test_list = [43, 25, 324, 234, 5, 2, 32423, 542, 534, 324, 23, 54, 65, 323, 42, 4,
#             123, 123, 5, 1, 321, 3124, 123, 123, 124, 1, 31, 23, 145, 3542, 43, 3, 21, 312]

# test_set = set(test_list)
# dlugosc_listy = len(test_list)
# dlugosc_setu = len(test_set)
# liczba_duplikatow = dlugosc_listy - dlugosc_setu
# print(liczba_duplikatow)

# a, b, c, = (1, 2, 3)
# print(type(a))

# data conversion exercise
# e_dict = {1:'one', 2: 'two', 3:'three'}
# check if a the key 1 exists in the dict
# print(1 in e_dict)
# sprawdzam_value = e_dict.values()
# print('four' in sprawdzam_value)

# testy na if elif oraz else proste if statements
# testuje do pierwszego spelnionego warnunku
# i nie bedzie sprawdzac dalej jesli jeden spelniony
# money_available = 15

# if money_available >= 85:
#  print("eat someting fancy")
# elif money_available > 45:
#  print("eat something nice")
# elif money_available > 15:
#  print("eat something okay")
# else:
#  print("eat something cheap")

# Bardziej skomplikowany if statement laczenie warunków
# Czyli and oraz or
# and oznacza ze i lewa i prawa musi byc spelniony jezeli jeden jest falszywy nie zadziala
# Or oznacza ze albo lewa albo prawa prawdziwa to dziala
# money_available = 100
# hungry = False
# bored = True
# if money_available > 80 and hungry == True: # Jeden z nich nie spelniony drugi i owszem nie wyswietli
#  print('to idz cos opierol 1')
# elif money_available > 80 or hungry == True:  # Mimo iz hungry nie jest true to tylko jeden spelniony
#  print('to idz cos opierol 2 ')
# elif money_available >80 or bored == True or hungry == True: # Nie wyswietla gdyz spelnil juz warunek wyzej mimo ze rowniez powinno go zwrocic
#  print("idz cos opierdol 3")


# Nesting if statements
# python jedzie od gory do  gowno glowny if statement
# pierwszy prawdziwy if drugi rowniez otrzymujemy nadal idzie  jednak drzewa znestowane nizej juz nie przechodza warunek nie spelniony
# dlatego gowno2 mimo prawdziwe rowniez nie przechodzi bo zostalo znestowane w warunku ktory wczesniej nie byl spelniony
# ptaki mialo ten sam poziom i zostal spelniony i zadzialal wiec python sprawdzal kazdy warunek oprocz tych znestowanych (chocby prawdziwy) w falszywym
# random_variable_1 = 3
# random_variable_2 = 'b'
# random_variable_3 = 15
# if random_variable_1 > 0:
#  print("gowno")
#  if random_variable_1 and random_variable_2 in ['a', 'b', 'c' ]:
#    print(" nadal idzie obydwa prawda")
#    if random_variable_3 != 15:
#      print("drzewa")
#      if random_variable_3 == 15:
#        print("gowno2")
#    if random_variable_1 == 3:
#     print("ptaki")
#      if random_variable_2 in ['b']:
#          print("ciasteczka")
# spierdalaj i nie indentuj komentarz
# nested wykonuje warunek po warunku zagniezdzony po zagniezdzonym az do falszywego wszystko zagniezdzone po falszywym jest o dupe potluc
# money_available = "gowno"
# hungry = False
# bored = True
# if money_available >= 80:
#  print("i have the money")
#  if hungry == True:
#    print("i'm hungry")
#    if bored == True:
#      print("eat something fancy")

# match money_available:
#  case 10:
#    print("gowno")
##  case 100:
#    print("mamy sporo kasy")
# case _:
#    print("nie mamy na to czasu")

# grade = 6
# match grade:
#  case 1:
#    print('pała siadaj')
#  case 2:
#    print("poszczescilo Ci sie")
#  case 3:
#   print("calkiem calkiem")
#  case 4:
#    print(" hoh ohoho")
#  case 5:
#    print("Powtorzysz to podejrzewam oszustwo")
#  case 6:
#    print(" Dobra robota")
#  case _:
#   print("TO NIE JEST OCENA SUKO")


# tworzenie listy od 0 do 100 while loop
# variable_for_boolean = 0
# list_for_exercise = [0]
# while variable_for_boolean <= 100:
#  variable_for_boolean += 1
#  list_for_exercise.append(variable_for_boolean)
#  if variable_for_boolean == 100:
#    print(list_for_exercise)
# tworzenie listy od 0 do 100 tylko z parzystymi
# variable_for_boolean = 0
# list_for_exercise = []
# while variable_for_boolean <= 100:
#  variable_for_boolean += 1
#  if variable_for_boolean % 2 == 0:
#    list_for_exercise.append(variable_for_boolean)
# print(list_for_exercise)

# list comprehension narazie za trudne i nie rozumiem syntaxu wrócę do tego
# list_for_exercise = [x for x in range(1,101) if x % 2 == 0  ]
# print(list_for_exercise)

# tylko parzyste od 0 do 100 ale bez 58
# variable_for_boolean = 0
# list_for_exercise = []
# while variable_for_boolean <= 100:
#  variable_for_boolean += 1
#  if variable_for_boolean % 2 == 0:
#    if variable_for_boolean == 58:
#      continue
#    list_for_exercise.append(variable_for_boolean)
# print(list_for_exercise)

# exercise
# practice_list = [[10, 40, 20, 50], [2, 42, 10], [101, 12, 4]]
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100
# for x in practice_list:
#  for x in x:
#    if x < 10:
#      continue
#    if x < 50:
#      print(x)
#    if x > 100:
#      break

# Funkcja prosty kalkulator ulepszony o standardową biblioteke
# def define - zdefiniuj
# funkcje calluje nazwa funkcji()
# w trakcie def funkcji nalezy podac jej argumenty te argument mogą mieć również przydzielone default value
# w trakcie callowania funkcji (juz bez def ) pasujemy jej parametry ktore nastepnie pozycjonalnie sa przypisywane do argumentow
# w trakcie callowania funkcji mozna rowniez podac kolejnosc za pomoca klucza np funkcja(arg1 = '')
# zeby zmieszac i pozycjonalne i keyowe najpierw musza isc pozycjonalne
# from operator import add, sub, mul, floordiv
# def calculator_plus(num1, num2, operation):
#  if operation == 'plus':
#    result_addition = add(num1, num2 )
#    print(f'{num1} + {num2} = {result_addition}' )
#  elif operation == 'minus':
#    result_extraction = sub(num1, num2)
#    print(f'{num1} - {num2} = {result_extraction}')
#  elif operation == 'multiply':
#    result_multiplication = mul(num1, num2)
#    print(f'{num1} * {num2} = {result_multiplication}')
#  elif operation == 'divide':
#    result_division = floordiv(num1, num2)
#    print(f'{num1} / {num2} = {result_division}')
#  else:
#    print('ERROR invalid function please provide a oper ation')

# calculator_plus(10,5,'divide')
# to bylo trudne zaczalem mieszac fstringa robiac dziwne rzeczy
# pozniej mialem problem z rozroznieniem callowania positional i key ale tak to powinno wygladac

# def greeter(person ='Person', greet ='Hello', weekday = 'Monday'):
#  print(f'{greet}, {person} Today is  {weekday} ')

# greeter('John', weekday = 'Piątek',greet ='Hi')

# def drzewo_nazw(**argument):
#  for arguments in argument:
#    print(argument)

# drzewo_nazw(arguments = [1, [1,2,3,4], 'drzewo'])


# def calculator_unlimited_num(*numbers,):
# print(sum(numbers))
# calculator_unlimited_num(1,2,3,)

#


# def fibonacci(n): # Definiuje funkcje fibonacci dla parametru N
#  if n <= 2:  # jezeli n jest mniejsze równe 2
#   return 1  # ma zwrócić jeden
#  else:
#    return fibonacci(n-1) + fibonacci(n-2) # zwraca fibonacci n-1 + fibonacci (n-2)
# print(fibonacci(1))


# FizzBuzz: Write a program that prints the numbers from 1 to 100.
# For multiples of three, print "Fizz" instead of the number.
# For multiples of five, print "Buzz" instead of the number.
# For numbers that are multiples of both three and five, print "FizzBuzz".

# import random
# def fizzbuzz_game(game):
#  game = random.randrange(0,100)
#  if game % 3 == 0 and game % 5 == 0:
#    print("FIZZBUZZ")
#  elif game % 3 == 0:
#      print("fizz")
#  elif game % 5 == 0:
#      print("buzz")
#  else:
#    print(game)
# fizzbuzz_game(1)

# def fizzbuzz_game (n):
#  if n % 3 == 0 and n % 5 == 0:
#    print("FIZZBUZZ")
#  elif n % 3 == 0:
#    print("fizz")
# elif n % 5 == 0:
#    print("Buzz")
#  else:
#    print(n)
# fizzbuzz_game(5)

# def fizzbuzz_game():
#  for number in range(1,101):
#    if number % 3 == 0 and number % 5 == 0:
#      print("FIZZBUZZ")
#    elif number % 3 == 0:
#      print("fizz")
#    elif number % 5 == 0:
#      print("buzz")
#    else:
#      print(number)
# fizzbuzz_game()

# multiplier = 3
# has_calculated = False
# def multiplication_calculator(number):
#  global has_calculated  # Access the global variable

# def contains_vowel(word): # Definiuje funkcje dla parametru word
#  vowel = ["a","e","i","o","u"] # Tworzę listę tych samogłosek jeżeli stworzę dla "aeiou" będzie źle bo stworzę listę z jednym elementem
#  # jeden element jedna iteracja, gdybym stworzył to jako sam string wtedy zwróciłby listę którą zrobiłem ręcznie
#  return any(letter in vowel for letter in word) # zwróć dla jakiekolwiek literki w samogłoska dla każdej literki w słowo

# print(contains_vowel("drzw"))

# def all_vowel(word: str) -> bool:
#  vowel = "aeiou"
#  return all(letter in vowel for letter in word)

# print(all_vowel(2))
# właśnie dostaliśmy faktury do opłacenia od różnych kontrahentów
# zebraliśmy je do kupy, ale chcemy jeszcze policzyć ile musimy zapłacić każdemu kontrahentowi!
# Ponadto, chcemy dowiedzieć się ile kasy musimy uzbierać na wszystkie te faktury 😮
# faktury = {
#    # firma : [kwota_faktury1, kwota_faktury2, ...]
#    "Windows" : [100, 50, 10, 123],
#     "Apple": [44, 33, 1220],
#   "Tesla": [1400, 50, 12, 2, 0, -1000],
#   "Huawei": [100, 50, 10],
# }

# 1. stwórz słownik 'sumy_faktur', który będzie wyglądał następująco:
# sumy_faktur = {


# }

# for firma, kwoty_faktury in faktury.items():
#  sumy_faktur.update({firma : sum(kwoty_faktury)})
#  print(faktury.items())

#   sumy_faktur[firma] = sum(kwoty_faktury)
# print(sumy_faktur)

# windows_list_of_values = faktury.get("Windows")
# apple_list_of_values = faktury.get("Apple")
# tesla_list_of_values = faktury.get("Tesla")
# huawei_list_of_values = faktury.get("Huawei")

# value_sum_microsoft = sum(windows_list_of_values)
# value_sum_apple = sum(apple_list_of_values)
# values_sum_tesla = sum(tesla_list_of_values)
# values_sum_huawei = sum(huawei_list_of_values)

# sumy_faktur.update({"Windows" : value_sum_microsoft, "Apple" : value_sum_apple, "Tesla" : values_sum_tesla, "Huawei" : values_sum_huawei})
# print(sumy_faktur)

# lista_wszystkich_kwot_dla_firm = sumy_faktur.values()
# total = sum(lista_wszystkich_kwot_dla_firm)
# sumy_faktur.update({"total" : total})
# print(sumy_faktur)
# Do sumowania wykorzystaj funkcję 'sum', która oczekuje, że wrzucisz do niej całą listę.
# przykład: # lista = [1,2,3]; # sum(lista) == sum([1,2,3]) == 6


# exercise
# create 2 global variables called 'multiplier' and has_calculated
# multiplier should have any integer and has_calculated should be set to the boolean False

# then create a function called multiply_calculator that takes one argument and calculates
# the multiplication of that number
# inside of the function multiply the parameter with the global variable multiplier
# once the calculation is done set has_calculated to True
# store that new number a variable called result and return it
# print the return value of the function (after it was called
# multiplier = 3
# has_calculated = False

# def multiply_calculator(multiply_by):
# global has_calculated

# has_calculated = True
# result = multiply_by * multiplier
# return result
# print(multiply_calculator(5))

# hello_bye = lambda number:  "hello" if number > 5 else "bye"
# print(hello_bye(6))
# inventory_names = ['Screws', 'Wheels', 'Metal parts',
#                   'Rubber bits', 'Screwdrivers', 'Wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]


# Exercise
# combine zip and enumerate to get 'Screws [id: 0] - inventory: 43'

# for id, inventory_tuple in enumerate(zip(inventory_names, inventory_numbers)):
#  print(f'{inventory_tuple[0]} [id:{id}] - quantity {inventory_tuple[1]}')
