from tkinter import *
import unittest
import project

class ProjectTest(unittest.TestCase):
    def test_ClassSetup(self):
        root = Tk()
        project.PasswordManager(root)
        root.mainloop()

    def test_lenght_password(self):
        root=Tk()
        test1 = project.PasswordManager(root)
        test1.quantity_password_gen_entry.get() == "21"
    
    def test_change_lenght(self):
        root=Tk()
        test2 = project.PasswordManager(root)
        test2.quantity_password_gen_entry.insert(0, "55")
        test2.generate_password()






if __name__ == "__main__":
    unittest.main()
