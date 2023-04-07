class Student:
    def __init__(self, name: str, surname: str, group: "Group" = None):
        self.name = name
        self.surname = surname
        self.group = group

    def __str__(self):
        group_name = self.group.name if self.group else "brak"
        return f"{self.name} {self.surname} ({group_name})"


class Group:
    def __init__(self, name: str, start_year: int, students: list[Student] = None):
        self.name = name
        self.start_year = start_year
        self.students = students or []

    def add_student(self, student: Student):
        if student in self.students:
            print(f"{student} już jest w grupie {self.name}.")
        elif student.group is not None:
            print(f"{student} należy już do innej grupy ({student.group.name}).")
        else:
            self.students.append(student)
            student.group = self

    def remove_student(self, student: Student):
        if student not in self.students:
            print(f"{student} nie należy do grupy {self.name}.")
        else:
            self.students.remove(student)
            student.group = None

    def __len__(self):
        return len(self.students)

    def __str__(self):
        return f"{self.name} <{len(self)}>"


# przykładowe użycie klas i metod
if __name__ == "__main__":
    # tworzymy dwie grupy i kilku studentów
    group1 = Group("IN-123", 2020)
    group2 = Group("IN-234", 2021)
    s1 = Student("Jan", "Kowalski")
    s2 = Student("Anna", "Nowak")
    s3 = Student("Adam", "Nowakowski")
    s4 = Student("Tomasz", "Kowalczyk")

    # dodajemy studentów do grupy 1
    group1.add_student(s1)
    group1.add_student(s2)
    group1.add_student(s3)
    group1.add_student(s4)

    # dodajemy studenta do grupy 2
    group2.add_student(s1)  # to się nie powinno udać, bo s1 jest już w grupie 1

    # usuwamy studenta z grupy 1
    group1.remove_student(s3)

    # wyświetlamy informacje o grupach i studentach
    print(group1)  # powinno wyświetlić "IN-123 <3>"
    print(group2)  # powinno wyświetlić "IN-234 <0>"
    print(s1)  # powinno wyświetlić "Jan Kowalski (IN-123)"
    print(s2)  # powinno wyświetlić "Anna Nowak (IN-123)"
    print(s3)  # powinno wyświetlić "Adam Nowakowski (brak)"
    print(s4)  # powinno wyświetlić "Tomasz Kowalczyk (IN-123)"
