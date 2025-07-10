class Marks:
    def __init__(self, mathmarks=0):
        self.mathmarks = mathmarks
    def update_marks(self,new_marks):
        if 0<=self.mathmarks<100:
            self.__mathmarks=new_marks
            print(f"Marks updated to {new_marks}")
        else:
            print("Marks not updated")
    def display_marks(self):
        print(f"marks updated to {self.__mathmarks}")

marks = Marks()
marks.display_marks()
marks.update_marks(100)
marks.display_marks()

