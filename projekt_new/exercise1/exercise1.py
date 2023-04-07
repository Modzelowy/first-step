"""
2. Napisz program, który przyjmuje jako argument nazwę pliku, a następnie przetworzy dane w nim zawarte.
https://www.kaggle.com/datasets/spscientist/students-performance-in-exams
dla każdego zagadnienia poniżej napisz funkcję, która:
    - przyjmie nazwę pliku, wczyta i zwróci dane w postaci listy wierszy. Użyj csv.DictReader, bądź csv.reader
    - obliczy średnią punktów z matematyki
    - obliczy liczbę uczniów dla każdego pochodzenia etnicznego
    - przyjmie jedno z ["math", "reading", "writing"] i wyświetli dane najlepszego ucznia
    -(BONUS)zaimplementuj 3 dodatkowe metody liczenia ilości wystąpień różnych grup etnicznych z wykorzystaniem 
    "from collections import defaultdict" i "from collections import Counter  dict.get, Counter, defaultdict"
"""
import csv
from collections import defaultdict
from collections import Counter


class Program:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.counter = 0
        with open(self.file_name, newline="") as self.the_file:
            self.read_obj = csv.reader(self.the_file, delimiter=";")
            self.wyniki_zmat = []
            self.wyniki_czyt = []
            self.wyniki_pis = []
            self.eth_list = []
            self.data = []
            for row in self.read_obj:
                self.data.append(row)
                self.counter += 1
                if self.counter == 1:
                    continue
                values = row[0].split(",")
                score_1 = int(values[5].replace('"', ""))
                score_2 = int(values[6].replace('"', ""))
                score_3 = int(values[7].replace('"', ""))
                eth_group = values[1]
                self.eth_list.append(eth_group)
                self.wyniki_zmat.append(score_1)
                self.wyniki_czyt.append(score_2)
                self.wyniki_pis.append(score_3)

            self.ilosc_ucznie = self.counter - 1

    def srednia(self):
        srednia_mat = sum(self.wyniki_zmat) / self.ilosc_ucznie
        print(srednia_mat)

    def eth_counter(self):
        counter = {}
        for group in self.eth_list:
            counter[group] = counter.get(group, 0) + 1
        print(counter)

    # def eth_counter(self):
    #     counter = defaultdict(int)
    #     for group in self.eth_list:
    #         counter[group] += 1
    #     print(counter)

    # def eth_counter(self):
    #     counter = Counter(self.eth_list)
    #     print(counter)

    # def eth_counter(self):
    #     a_counter = 0
    #     b_counter = 0
    #     c_counter = 0
    #     d_counter = 0
    #     e_counter = 0
    #     for group in self.eth_list:
    #         if "A" in group:
    #             a_counter += 1
    #         if "B" in group:
    #             b_counter += 1
    #         if "C" in group:
    #             c_counter += 1
    #         if "D" in group:
    #             d_counter += 1
    #         if "E" in group:
    #             e_counter += 1
    #     messages = [
    #         f"The A group has {a_counter} of students in test sample",
    #         f"The B group has {b_counter} of students in test sample",
    #         f"The C group has {c_counter} of students in test sample",
    #         f"The D group has {d_counter} of students in test sample",
    #         f"The E group has {e_counter} of students in test sample",
    #     ]
    #     for message in messages:
    #         print(message)

    def find_best(self, what_score):
        if what_score == "math score":
            indeks = self.wyniki_zmat.index(max(self.wyniki_zmat))
            print(
                self.data[indeks + 1]
            )  # do indeksu trzeba dodać jeden ze względu na to że indeksów w data jest 1001 a w self.wyniki jest 1000

        elif what_score == "reading score":
            indeks = self.wyniki_czyt.index(max(self.wyniki_czyt))
            print(self.data[indeks + 1])
        elif what_score == "writing score":
            indeks = self.wyniki_pis.index(max(self.wyniki_pis))
            print(self.data[indeks + 1])
        else:
            print(
                'Błędny parametr użyj jednego z  "math score" "reading score " " writing score" \n pamiętaj iż parametry są case sensitive '
            )


#
#   def __init__(self, file_name) -> None:
#         self.file_name = file_name
#         with open(self.file_name, newline="") as self.the_file:
#             read_obj = csv.reader(self.the_file, delimiter=";")
#             for row in read_obj:
#                 print(row)
# ['gender,"race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"']
# ['female,"group B","bachelor\'s degree","standard","none","72","72","74"']


program = Program("StudentsPerformance.csv")
program.eth_counter()
