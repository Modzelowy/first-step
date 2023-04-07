# lista = ["john", "sami", "adrian"]
# dictionary = {name.title(): len(name) for name in lista}


# for name in dictionary.keys():
#     print(f"name: {name}")

# for length in dictionary.values():
#     print(f"length: {length}")

# for items in dictionary.items():
#     print(f"items: {items}")

# # z duzej klucz
# #  ilosc znakow value
# 1. Napisz program, który:
#     - przetworzy dane z pliku names.txt tak, żeby imiona i nazwiska zaczynały się dużą literą, a reszta była małymi literami.
#     - zapisze dane do nowego pliku names.csv oddzielone średnikami ;
#     - pamiętaj, że plik csv w pierwszym rzędzie powinien zawierać nazwy kolumn
#     - wykorzystaj str.title()
# """

# # "some string".title()
# # 'Some String'
# # "qwe qwe".replace(" ", ";")
# # 'qwe;qwe'
# otwieramy plik wejściowy i wczytujemy dane
import csv

with open("names.txt", "r") as f:
    names = f.read().splitlines()

# przetwarzamy dane i zapisujemy do pliku csv
with open("names.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Imię", "Nazwisko"])  # nagłówek kolumn
    for name in names:
        first_name, last_name = name.split()
        first_name = first_name.title()
        last_name = last_name.title()
        writer.writerow([first_name, last_name])
