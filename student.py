class student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def showDetail(self):
        
        print("name :" + self.name)
        print("age :" + str(self.age))
        print("grade :" + str(self.grade))

stu1 = student("Brooke", 12,8)
stu1.showDetail()
stu2 = student("Rae",8,4)
stu2.showDetail()
print(stu1.age)