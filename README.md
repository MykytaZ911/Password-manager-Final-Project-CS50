Password Manager


Video Demo URL: https://youtu.be/4XbQKfkUSOc

Description:
    This program is Password Manager based on the Tkinter library. I used Tkinter for the User Interface, Random library for generating passwords, and CSV library for saving passwords.

 My program has Enteries: Service, Login, and Password. The first time when you save the first service, the program will check if a file called passwords.csv exists or not; if not program will create this file and save information. 
 The program contains check button parameters for generating passwords such as big letters, small letters, numbers, and symbols. By default, the password length is 21 symbols, but you can change it in the entry "Quantity Symbols." It has to be one or more, but less than fifty-one. 
 A random library generates the password, and each symbol is randomly chosen from a list of all symbols that were chosen in check buttons. 
 Service was created, such as a label for login and password. We may forget our password or login, but we have to remember the service. You may name the Service - Google or Google1, Google2, etc. 
 Button Search is looking for service in a CSV file, and it doesn't matter if it is lower or upper case ("Be aware of meaning, because Google and google are the same for this program"). The program will represent the file in entries if the file contains this service.
 Each data is saved in DictWriter in mode "w+." So, whenever you want to add or update login info, dictWriter will rewrite the whole file. First, DictReader will read a file, and each line will be saved in the list variable and checked for the same service. If the service is found, you will be asked to update the password or not; otherwise, it will added to the end of the list. After all, DictWriter will rewrite the whole file.