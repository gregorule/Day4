class Student:

    def __init__(self, name = "Student", age = "Student", cohert = "Student"):
        self.name = name
        self.age = age
        self.cohert = cohert

    def final(self, test1, test2, test3):
        avg = (test1 + test2 + test3)/3
        return f"{self.name} your average score is: {avg}"

John = Student("John", "21", "22AprEnable3")
Jane = Student("Jane", "22", "22AprEnable3")

print(getattr(John, "age"))
print(getattr(Jane, "cohert"))
print(John.final(15,25,30))


