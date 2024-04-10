#User
import datetime
from Book import *
from Library import *


class User(object):  #class for all types of users in a list and books borrowed in a list

    def __init__(self,Name: str, ID: int, BooksBorrowed: str, Email: str,age,credit_card,social_security,area,restricted=False):
        self.Name = Name
        self.ID = ID
        self.BooksBorrowed = BooksBorrowed
        self.Email = Email
        self.area = area
        self.age = age
        self.credit_card = credit_card
        self.social_security = social_security
        self.restricted = restricted #setting default that user isnt restricted


    def get_name(self):
        return self.Name

    def get_ID(self):
       return self.ID

    def get_BooksBorrowed(self):
       return self.BooksBorrowed

    def get_Email(self):
        return self.Email

    def get_area(self):
        return self.area

    def get_credit_card(self):
        return self.credit_card

    def get_social_security(self):
        return self.social_security

    def get_age(self):
        return self.age

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#first subclass "Normal User"
class NormalUser(User):    # the Normal user class and its parameters
    def __init__(self, Name: str, ID: int, BooksBorrowed: str, Email: str,age,credit_card,social_security,area,restricted=False):
        super(NormalUser, self).__init__(Name, ID, BooksBorrowed, Email,age,credit_card,social_security,area,restricted)
        #includes the things previously declared within the parent

    def BorrowBook(self, book: Book):  # incrementing by one when borrrowing a book
            book.NoCopiesBorrowed -= 1
        # check loop then if available first

    def ReturnBook(self, book: Book):  # decrementing by one when returning book
        book.NoCopiesBorrowed += 1

    def SearchBook(self, searchbook: str):  # searching books
        for j in Book.booklist:
            if j.Title == searchbook:
                return True
            else:
                return False

    def ExtendLoan(self, newloan: int, book: Book):
        book.LoanPeriod += newloan


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#second subclass "Librarian
class Librarian(User):    # the Librarian class and its parameters
    def __init__(self, Name: str, ID: int, BooksBorrowed: str, Email: str, age, credit_card, social_security,area,restricted=False):
        super(Librarian, self).__init__(Name, ID, BooksBorrowed, Email, age, credit_card, social_security,area,restricted)

    def SearchBook(self, searchbook: str):  # searching books
        for j in Book.booklist:
            if j.Title == searchbook:
                return True
            else:
                return False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#third subclass "System Domain"
class SystemDomain(User):   # the System domain class and its parameters
    def __init__(self, Name: str, ID: int, BooksBorrowed: str, Email: str, age, credit_card, social_security,area,restricted=False):
        super(SystemDomain, self).__init__(Name, ID, BooksBorrowed, Email, age, credit_card, social_security,area,restricted)

    def add_user(self,name,id,user_type,email,age,credit_card,security_number):
        new_user=User(name,id,user_type,email,age,credit_card,security_number)
        for i in mainsystem.user:
            for j in mainsystem.user:
                if j == name and j==id:
                    print("user already registered")
                else:
                     mainsystem.user.append(new_user)
                     print("adding them bestie")

    def remove_user(self):
        emailsearch = input("please enter user's email ")
        for i in mainsystem.user:
            if emailsearch == i.Email:  # looking for the user by email
                mainsystem.user.pop(mainsystem.user.index(i))  # removing or "popping" the user found by the given email found
                print("done!!!!!!!!!!!!!")
                break
            else:
                print("user not found :(")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Student(User):
    def __init__(self, Name: str, ID: int, BooksBorrowed: str, Email: str, age, credit_card, social_security,area,restricted=False):
        super(Student, self).__init__(Name, ID, BooksBorrowed, Email, age, credit_card, social_security, area,restricted)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# lara = NormalUser("lara",254,"lala","laouda@") #example of user
# book1 = Book("book1","me",64846,15,True,"bla") #example of book
# legendsandlattes = Book("legends and lattes","Travis  Baldree",9798985663211,45,True,"him")

# a list of different users and their information
# users_List = [NormalUser("lily", 254, "book1", "lily@"), Librarian("lara", 364, "book2", "lara@"), SystemDomain("farhoud", 676, "book3", "farhoud@")]


