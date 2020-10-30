



class School:
    def __init__(self, name, stud_list):
        self.stud_list=stud_list
        self.name_school=name


class Student:
    def __init__(self,name, surname, classes):
        self.name=name
        self.surname=surname
        self.classes=[]
        self.classes.append(classes)

    def add_class(self, class_new):
        self.classes.append(class_new)

    def count_attendace(self):
        total=0
        for x in self.classes:
            total+=x.attendance

        print(len(self.classes)/total*100)



class Class_stud:
    def __init__(self, name, attendance=None, grade=None):
        self.name=name
        self.attendance=attendance
        self.grade=grade

    def check_attendance(self):
        self.attendance=1


class1=Class_stud('math')
stud1=Student('John','Smith',class1)
stud1.classes[0].check_attendance

school= School('highschool', stud1)
stud1.count_attendace

    


