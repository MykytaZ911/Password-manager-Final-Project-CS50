from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os
import random



class PasswordManager:
    def __init__(self, root):
        root.title("Password Manager")

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        
        # Entries
        self.service = StringVar()
        self.service_entry = ttk.Entry(mainframe, width=30, textvariable=self.service)
        self.service_entry.grid(column=1, row=1)
        ttk.Label(mainframe, text="Service").grid(column=1, row=0)

        self.login = StringVar()
        self.login_entry = ttk.Entry(mainframe, width=30, textvariable=self.login)
        self.login_entry.grid(column=1, row=3 )
        ttk.Label(mainframe, text="Login").grid(column=1, row=2)

        self.password = StringVar()
        self.password_entry = ttk.Entry(mainframe, width=30, textvariable=self.password )
        self.password_entry.grid(column=1, row=5)
        ttk.Label(mainframe, text="Password").grid(column=1, row=4)

        self.quantity_password_gen = StringVar()
        self.quantity_password_gen_entry = ttk.Entry(mainframe, width=5, textvariable=self.quantity_password_gen)
        self.quantity_password_gen_entry.grid(column=2, row=5)
        ttk.Label(mainframe, text="Quantity Symbols").grid(column=2, row=4)
        # Default value for the number of characters
        self.quantity_password_gen_entry.insert(0, "21")

        # Check buttons
        self.big_letter_var = BooleanVar(value=True)
        self.small_letter_var = BooleanVar(value=True)
        self.numbers_var = BooleanVar(value=True)
        self.symbols_var = BooleanVar(value=True)


        b_letters = ttk.Checkbutton(mainframe, text="Big letters", variable=self.big_letter_var, onvalue=True)
        b_letters.grid(column=0, row=6, sticky=W)

        s_letters = ttk.Checkbutton(mainframe, text="Small letters", variable=self.small_letter_var, onvalue=True)
        s_letters.grid(column=0, row=7, sticky=W)

        numbers = ttk.Checkbutton(mainframe, text="Numbers", variable=self.numbers_var, onvalue=True)
        numbers.grid(column=0, row=8, sticky=W)

        symbols = ttk.Checkbutton(mainframe, text="Symbols", variable=self.symbols_var, onvalue=True)
        symbols.grid(column=0, row=9, sticky=W)

        # Button for passworg generating
        generate = ttk.Button(mainframe, text="Generate", command=self.generate_password)
        generate.grid(column=1, row=6, sticky=N)

        # Save Login Info
        save = ttk.Button(mainframe, text="Save", default="active", command=self.save)
        save.grid(column=1, row=7, sticky=N)

        # Search Service 
        search = ttk.Button(mainframe, text="Search", command= self.search)
        search.grid(column=2, row=1, sticky=N)
        

        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=5)
        


    def save(self):
        is_new_data_appended = False
        fieldnames = ["service", "login", "password"]
        is_file_exist = os.path.isfile("passwords.csv")
        data = []
        
        service = self.service.get().lower().strip()
        login = self.login.get().strip()
        password = self.password.get().strip()
        
        try:
            if len(service) < 1 or len(login) < 1 or len(password) < 1:
                raise ValueError
            if is_file_exist == False:
                self.create_csv(fieldnames)

            with open("passwords.csv", "r") as file_for_copy:
                reader = csv.DictReader(file_for_copy, fieldnames=fieldnames)
                for row in reader:
                    if row["service"] == service:
                        check = messagebox.askyesno(message="Do you want to update your data for this service?")
                        if check:
                            is_new_data_appended = True
                            data.append({"service": service, "login": login, "password": password})
                        else:
                            return 0
                    else:
                        data.append(row)

                if is_new_data_appended == False:
                    data.append({"service": service, "login": login, "password": password})

            self.service_entry.delete(0, "end")
            self.login_entry.delete(0, "end")
            self.password_entry.delete(0, "end")

            with open("passwords.csv", "w+", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)

                for i in data:
                    writer.writerow(i)
            messagebox.showinfo(message="Password saved")

        except:
            messagebox.showerror(message="Password not saved")

        
    def create_csv(self, f):
        with open("passwords.csv", "w", newline="") as new_file:
            new_writer = csv.DictWriter(new_file, fieldnames=f)
            new_writer.writeheader()


    def search(self):
        try:
            search_service = self.service.get().lower()
            with open("passwords.csv", "r") as search:
                search_reader = csv.DictReader(search, fieldnames = ["service", "login", "password"])
                for row in search_reader:
                    if row["service"] == search_service:

                        self.login_entry.delete(0, "end")
                        self.password_entry.delete(0, "end")

                        self.login_entry.insert(0, row["login"])
                        self.password_entry.insert(0, row["password"])
        except:
            messagebox.showerror(message="You don't have any passwords")


    def generate_password(self):
        letters_ls = "qwertyuiopasdfghjklzxcvbnm"
        numbers_ls = "1234567890"
        symbols_ls = "!@#$%^*+-_="
        mix = ""
        password = ""


        big_letters = self.big_letter_var.get()
        small_letter = self.small_letter_var.get()
        numbers = self.numbers_var.get()
        symbols = self.symbols_var.get()
        try:
            quantity = int(self.quantity_password_gen_entry.get())
            if quantity > 52 or quantity < 1:
                raise ValueError
        except:
            return messagebox.showwarning(message="Enter the correct quantity")

        if big_letters == True:
            mix+=letters_ls.upper()
        if small_letter == True:
            mix+=letters_ls
        if numbers == True:
            mix+=numbers_ls
        if symbols == True:
            mix+=symbols_ls

        if mix == "":
            return messagebox.showwarning(message="Too few options")
        
        
        items = random.choices(list(mix), k=quantity)
        password = "".join(items)

        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

    



if __name__ == "__main__":
    root = Tk()
    PasswordManager(root)
    root.mainloop()