from gta6 import GTA6, Student

class Main:
    def __init__(self):
        self.game = GTA6()
        self.game.start()
        self.student_info()

    def student_info(self):
		# Student("Ім'я", Вік, Курс)
        student1 = Student("Олексій", 15, 1)
        print(student1.get_info())
        student1.change_course(2)
        print(student1.get_info())
        
        student2 = Student("Іван", 16, 2)
        print(student2.get_info())
        student2.change_course(3)
        print(student2.get_info())

if __name__ == "__main__":
    Main()
