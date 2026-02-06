class Student:
    def init(self, name, group, avg):
        self.name = name
        self.group = group
        self.avg = avg

    def show_info(self):
        print(f"Name: {self.name}, Group: {self.group}, Average grade: {self.avg}")


s1 = Student("Amogus", "1", 4.3)
s2 = Student("Abobus", "2", 4.7)

s1.show_info()
s2.show_info()
