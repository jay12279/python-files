#Program.2
#student class with marks and percentage
class Student:
    def __init__(self, name, marks):
        self.name = name #stores the student name
        self.marks = marks  # list of marks

    def calculate_percentage(self):
        total = sum(self.marks) #adds all the marks
        self.percentage = total / len(self.marks) #count show many subjects and calculates the average
        return self.percentage 

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Overall Percentage: {self.calculate_percentage():.2f}%")


student1 = Student("Zukerberg", [85, 90, 78, 92, 88])
student1.display()
