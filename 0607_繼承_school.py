class School(object):
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []

    def enroll(self, stu_obj):
        print("為學員%s辦理註冊手續" % stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        print("雇用新員工 %s" % staff_obj.name)
        self.staffs.append(staff_obj)



class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self, name, age, sex, salary, course):
        super(Teacher, self).__init__(name, age, sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''
        ---- info of Teacher : %s
        Name : %s
        Age : %s
        Sex : %s
        Salary : %s
        Course : %s
        
        ''' % (self.name,self.name, self.age, self.sex, self.salary, self.course))

    def teach(self):
        print("%s is teaching course [%s]" % (self.name, self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex, std_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.std_id = std_id
        self.grade = grade

    def tell(self):
        print('''
        ---- info of Student : %s ----
        Name : %s
        Age : %s
        Sex : %s
        student_ID : %s
        Grade : %s

        ''' % (self.name,self.name, self.age, self.sex, self.std_id, self.grade))

    def pay_tuition(self, amount):
        print("%s has paid tuition $%s" % (self.name, amount))


school = School("老男孩IT","沙河")

t1 = Teacher("Oldboy",56,"MF",20000,"Linux")
t2 = Teacher("Alex",22,"M",3000,"Python")

s1 = Student("Leon",30,"M",1001,"python")
s2 = Student("Leo",24,"M",1002,"python")

t1.tell()
s1.tell()

school.enroll(s1)
school.enroll(s2)
school.hire(t1)

print(school.students)
print(school.staffs)

school.staffs[0].teach()

for stu in school.students:
    stu.pay_tuition(5000)