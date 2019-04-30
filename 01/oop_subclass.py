# coding=UTF-8

class SchoolMember:
    '''代表学校里的任何成员'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    
    def tell(self):
        ''''告诉有关我的细节'''
        print('Name: "{}", Age: "{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''代表一位老师'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialzed Teacher: {})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    ''' 代表一位学生'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))


# test

t = Teacher('Mrs. Shrividya',40, 3000)
s = Student('Swaroop', 23, 75)
print()
members = [t, s]
for member in members:
    member.tell()