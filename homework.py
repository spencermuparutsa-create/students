class employee():

    def __init__(self,name,department,ID,location):
        self.name = name
        self.department = department
        self.ID = ID
        self.location = location

    def showDetail(self):

        print("name:" + self.name)
        print("department:" + self.department)
        print("ID:" + str(self.ID))
        print("location:" + self.location)
    def changelocation(self):
        loca = input("What is your new location?:")
        self.location = loca
work1 = employee("Brooke","coding",829350,"Italy")
work1.showDetail()
work1.changelocation()
work1.showDetail()
