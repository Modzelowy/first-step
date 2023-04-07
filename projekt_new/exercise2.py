"""url_reqres = "https://reqres.in/api/users"
url_gorest = "https://gorest.co.in/public/v2/users"

# zainstaluj paczkę requests https://pypi.org/project/requests/.
# pobieraj dane requests.get i zapisz do zmiennej używając dane = zmienna.json()
# 1. pobierz dane z gorest i zapisz do csv:  imie, nazwisko (przyjmij, że to pierwsze 2 oddzielone spacją wyrazy)
# 2. pobierz dane również z gorest i złącz w jednym pliku (uważaj, nazwy różnią się)
# 3. reqres przyjmuje query parameter np "?page=2" w https://reqres.in/api/users?page=2
#    wczytaj wszystkie dostępne dane
"""
import requests
import csv

url_reqres = "https://reqres.in/api/users"
url_gorest = "https://gorest.co.in/public/v2/users"


dane = requests.get(url_reqres)
