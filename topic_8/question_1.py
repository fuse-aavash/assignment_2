class University:
    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        self.__departments = []

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print(f" - {department.get_department_name()}")

class Department(University):
    def __init__(self, name, head_of_department):
        super().__init__("University of Newyork", "New York ")  # Default university name and location
        self.__department_name = name
        self.__head_of_department = head_of_department
        self.__courses_offered = []

    def add_course(self, course):
        self.__courses_offered.append(course)

    def get_department_name(self):
        return self.__department_name

    def display_details(self):
        print(f"Department Name: {self.__department_name}")
        print(f"Head of Department: {self.__head_of_department}")
        print("Courses Offered:")
        for course in self.__courses_offered:
            print(f" - {course}")


# Create a University object
university = University("University of Nepal", "City ABC")

# Create Department objects
department1 = Department("Computer Science", "Dr. Smith")
department2 = Department("Physics", "Prof. Johnson")

# Add departments to the university
university.add_department(department1)
university.add_department(department2)

# Add courses to the departments
department1.add_course("Introduction to Programming")
department1.add_course("Data Structures and Algorithms")
department2.add_course("Classical Mechanics")
department2.add_course("Quantum Physics")

# Display details of the university and departments
university.display_details()
print("\n")
department1.display_details()
print("\n")
department2.display_details()
