class Human:
    def __init__(self,age,name):
        self.age = age
        self.name = name
    def intro(self):
        print(str(self.age)+"살" + self.name + "입니다")

sang = Human(29,'김상형')
sang.intro()

class Student(Human):
    def __init__(self,age,name,stunum):
        super().__init__(age,name)
        self.stunum = stunum

    def intro(self):
        super().intro()
        print("학번:"+str(self.stunum))

lee = Student(19,"리",1904110)
lee.intro()