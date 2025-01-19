"""
Question2: Create a "School" class in Python. This class should have the following features and functionality:

Features:
"name"
"foundation_year"
"students"
"teachers"
Methods:
add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
view_teacher_list(self): A method used to display the list of teachers working in the school. List teacher names and majors.
"""
class School:
    def __init__(self, name, foundation_year, students = [], teachers=[]):
        self.name = name
        self.foundation_year = foundation_year
        self.students = students
        self.teachers = teachers
    
    def add_new_student(self, student_name, student_class):
        self.students.append({"name": student_name, "class": student_class})
    
    def add_new_teacher(self, teacher_name, teacher_branch):
        self.teachers.append({"name": teacher_name, "branch": teacher_branch})

    def view_student_list(self):
        print("Student List:")
        for student in self.students:
            print(f"Name: {student['name']}, Class: {student['class']}")

    def view_teacher_list(self):
        print("Teacher List:")
        for teacher in self.teachers:
            print(f"Name: {teacher['name']}, Branch: {teacher['branch']}")

if __name__ == "__main__":
        school = School("Example School", 2023)
        school.add_new_student("Omer Sami", "10th Grade")
        school.add_new_teacher("Mustafa Gundogdu", "Mathematics")
        print("----------------------------------")
        school.view_student_list()
        print("----------------------------------")
        school.view_teacher_list()
        print("----------------------------------")
        input()