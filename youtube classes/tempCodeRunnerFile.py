class Student:
    def __init__(self, fullname):
        self.name = fullname
        print(f"Adding new student {self.name} to the database")

s1 = Student("Karan")
