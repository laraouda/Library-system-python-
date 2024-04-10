# ____________________
# Assignment 2
# Written by: Lara Ouda 202100680
# _____________________
import datetime
import json
import mainsystem
from Book import *
from User import *

#Start of Assignment 2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#making the library class

class Library(object):
    def __init__(self, library_name:str, library_type:str,user_type:str):
        self.library_name = library_name
        self.library_type = library_type
        self.user_type = user_type  #ask which one
        self.users_list=[]
        self.books_library=[]
        self.active_loans=[]
        self.borrow_policy=[3,5,1]    #setting 3,5 and 1 as defaults
    #Borrow policy [0] is the loan period, [1] is the grace period, [2] is the no of times to extend loan


    #setting normal setters and geters for library name, library type, user type
    def get_library_name(self):
        return self.library_name

    def set_library_name(self, new_library_name):
          self.library_name=new_library_name

    def get_library_type(self):
        return self.library_type

    def set_library_type(self, new_library_type):
        self.library_type=new_library_type

    def get_user_type(self):
        return self.user_type

    def set_user_type(self, new_user_type):
        self.user_type=new_user_type

    def get_loan_period(self):
        return self.borrow_policy[0]

    def set_loan_period(self,new_loan):
        self.borrow_policy[0]=new_loan

    def get_grace_period(self):
        return self.borrow_policy[1]

    def set_grace_period(self,new_grace):
        self.borrow_policy[1]=new_grace

    def get_extend_time(self):
        return self.borrow_policy[2]

    def set_extended_time(self,new_time):
        self.borrow_policy[2]=new_time


#adding a user and info needed
    def add_user(self,name,id,user_type,email,age,credit_card,security_number,Area):
        for i in range(len(self.registered_user)):
            if self.registered_user[i].get_name() == name and self.registered_user[i].get_ID() == id: # check user is in the registered users list
                print("user already registered")
            elif self.registered_user[i].get_name() != name and self.registered_user[i].get_ID() != id and i == len(self.registered_user)-1:

                for j in range(len(mainsystem.users)):
                    if mainsystem.users[j].get_name() == name and mainsystem.users[j].get_ID()==id:
                        print("user already registered")
                    elif mainsystem.users[j].get_name() != name and mainsystem.users[j].get_ID()!=id and j == len(mainsystem.users)-1:
                        if user_type == "System Admin":
                            useradded=SystemDomain(name,id,user_type,email,age,credit_card,security_number,Area)
                            self.registered_user.append(useradded)
                            mainsystem.user_list.append(useradded)
                            print("adding them bestie")

                        elif user_type == "Librarian":
                            useradded = Librarian(name, id, user_type, email, age, credit_card, security_number,Area)
                            self.registered_user.append(useradded)
                            mainsystem.user_list.append(useradded)
                            print("adding them bestie")

                        elif user_type == "Normal User":
                            useradded = NormalUser(name, id, user_type, email, age, credit_card, security_number,Area)
                            self.registered_user.append(useradded)
                            mainsystem.user_list.append(useradded)
                            print("adding them bestie")

                        elif user_type == "Student":
                            useradded = Student(name, id, user_type, email, age, credit_card, security_number,Area)
                            self.registered_user.append(useradded)
                            mainsystem.user_list.append(useradded)
                            print("adding them bestie")

    def remove_user(self,email):
        for i in mainsystem.users:
            if email == i.Email:  # looking for the user by email
                mainsystem.users.pop(mainsystem.users.index(i))  # removing or "popping" the user found by the given email found
                print("done!!!!!!!!!!!!!")
                break
            else:
                print("user not found :(")

    def add_book(self,book_added):
        Book.booklist.append(book_added)    #adding the new book to book list
        print(Book.booklist)

    def remove_book(self,Remove_Book):
        for i in Book.booklist:
            if Remove_Book == i.Title:  # searching for book using title
                Book.booklist.pop(Book.booklist.index(i))  # removing or "popping" from book list
                print("Book has been removed")
                break
        else:
            print("Book not found :(")


    #def restrict_user(self):



    # def remove_book(self):
    #     Remove_Book = input("Enter book name")
    #     for i in Book.booklist:
    #         if Remove_Book == i.Title:  # searching for book using title
    #             Book.booklist.pop(Book.booklist.index(i))  # removing or "popping" from book list
    #             print("Book has been removed")
    #             break
    #     else:
    #         print("Book not found :(")

    def borrow_book(self,book, user: User):  #input the user that wants to borrow
        Book_Borrowed = input("What book would you like to borrow? ")
        if user.SearchBook(Book_Borrowed):
            for i in range(len(self.books_library)):
                if self.books_library[i].Title == Book_Borrowed:  # searching for the book title in the list of books to check if available
                    user.BorrowBook(self.books_library[i])
                    self.active_loans.append(self.books_library[i])
                    self.books_library.pop(i)
                    print(self.books_library[i].NoCopiesBorrowed)
                    print("Done! :)")
                else:
                    print("sorry book not available right now :'(")

    def return_book(self,book,user:User):  #input the user that wants to return
        Book_Returned = input("what book would you like to return? ")
        if user.SearchBook(Book_Returned):
            for i in range(len(self.books_library)):
                if self.books_library[i].Title == Book_Returned:  # searching for the book title in the list of books to check if available
                    user.ReturnBook(self.books_library[i])
                    self.books_library.append(self.books_library[i])
                    self.active_loans.pop(i)
                    print(self.books_library[i].NoCopiesBorrowed)
                    print("Done! :)")
                else:
                    print("sorry book not available right now :'(")


    def search_book(self,booksearch):
        if mainsystem.user[mainsystem.userindex].SearchBook(booksearch):  # searching for the book
            print("Book Found")
        else:
            print("Sorry, book not found :(")

    #def get_library_stats(self):


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#inheritence 1 school library
class School_Library(Library):
    def __init__(self,library_name,library_type,user_type,name, id, email, type, Area, Age, credit_card):
        super(School_Library, self).__init__(library_name,library_type,user_type)
        self.name=name
        self.id=id
        self.email=email
        self.type=type
        self.Area=Area
        self.Age=Age
        self.credit_card=credit_card
        self.security_number=0

#polymorphisim
    def add_user(self, name, id, email, type, Area, Age, credit_card, security_number):
        if type == "Admin" or type == "Student" or type == "Librarian":
            super(School_Library, self).add_user(name, id, email, type, Area, Age, credit_card, security_number)
            print("Okay")
        else:
            print("That User Is Not Allowed To Be Created!!")

    def borrow_book(self,book,user):
        x = user.__class__.__name__  # assigning x to the type of user found
        if x == "Student" and not user.restricted:
            super(School_Library, self).borrow_book(book,user)

    # def return_book(self,book,user,newloanperiod):
    #     if newloanperiod -self.borrow_policy[0] >0:
    #         user.restricted =True
    #     else:
    #         for i in Book.booklist:
    #             if i in Book.booklist:
    #                 book.NoCopiesBorrowed -= 1


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#inheritence 2 Minicipal library
class Municipal_Library(Library):
    def __init__(self, library_name, library_type, user_type, name, id, email, type, Area, Age, credit_card):
        super(Municipal_Library, self).__init__(library_name, library_type, user_type)
        self.name = name
        self.id = id
        self.email = email
        self.type = type
        self.Area = Area
        self.Age = Age
        self.credit_card = credit_card
        self.security_number = 0

    def add_user(self,name,id,user_type,email,age,credit_card,security_number,Area):
        if Area==self.Area:
            super(Municipal_Library, self).add_user(name,id,user_type,email,age,credit_card,security_number,Area)

        else:
            print("Sorry user is in a different area :////")

    def borrow_book(self,book,user):
        if user.credit_card != None:
            super(Municipal_Library, self).borrow_book(book,user)
        else:
            print("sorry you are poor :(")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#inheritence 3 National library
class National_Library(Library):
    def __init__(self, library_name, library_type, user_type, name, id, email, type, Area, Age, credit_card):
        super(National_Library, self).__init__(library_name, library_type, user_type)
        self.name = name
        self.id = id
        self.email = email
        self.type = type
        self.Area = Area
        self.Age = Age
        self.credit_card = credit_card
        self.security_number = 0
    def add_user(self,name,id,user_type,email,age,credit_card,security_number,area):
         if self.security_number == security_number:
             super(National_Library, self).add_user(name,id,user_type,email,age,credit_card,security_number,area)
             print("User has been added sucessfully :)")
         else:
             print("no security number, go back to where you came from :)")

    def borrow_book(self, book, user):
        if user.credit_card != None:
            super(National_Library, self).borrow_book(book, user)
        else:
            print("sorry you are poor :(")

