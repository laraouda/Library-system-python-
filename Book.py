# ____________________
# Assignment 2
# Written by: Lara Ouda 202100680
# _____________________
import datetime
import json


# booklist = ["book1",["book1","me",64846,4,8,15,True,2],"book2",["book2","you",8456,4,6,False,3]]  #list of books input

# declaring the class "book"
class Book:
    def __init__(self, Title: str, Author: str, ISBN: int, TotalCopies: int, Online, BorrowerInfo: str):
        # declaring the parameters for the books
        self.Title = Title
        self.Author = Author
        self.ISBN = ISBN
        self.TotalCopies = TotalCopies
        self.NoCopiesBorrowed = 0
        self.NoCopiesAvail = self.TotalCopies - self.NoCopiesBorrowed
        self.Online = True if Online == True or Online.lower() == "true" else False
        self.LoanPeriod = 3
        self.BorrowerInfo = BorrowerInfo


#     def __str__(self):
# #to assure the output is in str format
#         return f'{self.Title},{self.Author},{self.NoCopiesAvail},' \
#                f'{self.NoCopiesBorrowed},{self.TotalCopies},{self.Online},' \
#                f'{self.LoanPeriod},{self.BorrowerInfo}'

    def get_title(self):
        return self.Title

    def get_copies(self):
        return self.NoCopiesAvail

    def BorrowBook(self, book):  # incrementing by one when borrrowing a book
        book.NoCopiesBorrowed += 1
        # check loop then if available first

    def ReturnBook(self, book):  # decrementing by one when returning book
        book.NoCopiesBorrowed -= 1

    def SearchBook(self, searchbook: str):  # searching books
        for j in Book.booklist:
            if j.Title == searchbook:
                return True
            else:
                return False


    def __dict__(self):
        return {
            "title":self.Title,
            "author":self.Author,
            "ISBN":self.ISBN,
            "Total copies":self.TotalCopies,
            "Copies avaiabe":self.NoCopiesAvail,
            "loan period":self.LoanPeriod
        }