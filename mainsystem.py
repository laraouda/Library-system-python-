#Main system
from Library import *
from User import *
import datetime
import json
booklist = []

users = [NormalUser("lara", 254, "lala", "laouda@",19,"035165","degla","03465"), Librarian("ahmed", 364, "book2", "ahmed@",45,"tagamo3","9435","6844"), SystemDomain("mohamed", 676, "book3", "mohamed@",34,"zayed","684545","64545"),Student("bruh",464,"book4","bruh@",22,"6845","684531","Municipal")]

#
# all_users = {"users": []}
# data_holder = all_users["users"]
# with open('data.json', 'r') as f:
#     data2 = json.load(f)
#     for obj in data2['users']:
#         if obj['type'] == "Student":
#             u= Student(**obj["user_data"])
#             users.append(u)
#         elif obj['type'] == "Librarian":
#             u= Librarian(**obj["user_data"])
#             users.append(u)
#         elif obj['type'] == "SystemDomain":
#             u= SystemDomain(**obj["user_data"])
#             users.append(u)
#         elif obj['type'] == "NormalUser":
#             u= NormalUser(**obj["user_data"])
#             users.append(u)
# print(users)
#
# all_books = {"books": []}
# data_holder = all_books["books"]
# with open('books.json', 'r') as f:
#     for book in Book.booklist:
#         data = {"book_data": book.__dict__}
#         data_holder.append(data)
#         json_string = json.dumps(all_books, indent=4)
#         f.write(json_string)

#append loading mara book w mara user

# def writeusers(filename, L):
#     with open(filename, 'w') as file:
#         s = "{\"Users\":[\n"
#
#         for i in L:
#             jsonstr = json.dumps(i,default= lambda o : o.__dict__)
#             s += jsonstr + "," + "\n"
#
#         s += "\n]}"
#         file.write(s)
#         file.close()
#
#
# def writeBooks(filename, L):
#     with open(filename, 'w') as file:
#         s = "{\"Books\":[\n"
#
#         for i in L:
#             jsonstr = json.dumps(i.__dict__())
#             s += jsonstr + "," + "\n"
#
#         s += "\n]}"
#         file.write(s)
#         file.close()
#
#
# def writeLibrary(filename, L):
#     with open(filename, 'w') as file:
#         s = "{\"Library\":[\n"
#
#         for i in L:
#             jsonstr = json.dumps(i.__dict__())
#             s += jsonstr + "," + "\n"
#
#         s += "\n]}"
#         file.write(s)
#         file.close()
def save():
    all_users = {"users": []}
    data_holder = all_users["users"]
    with open('user.json', 'w') as f:
        for user in users:
            data = {"user_data": user.__dict__, "type": user.__class__.__name__}
            data_holder.append(data)
        json_string = json.dumps(all_users, indent=4)
        f.write(json_string)

    all_books = {"books": []}
    data_holder = all_books["books"]
    with open('books.json', 'w') as f:
        for book in booklist:
            data = {"book_data": book.__dict__}
            data_holder.append(data)
        json_string = json.dumps(all_books, indent=4)
        f.write(json_string)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
try:
    print(" 1-school library\n 2-Municipal Library\n 3-National Library")
    answer=input("hello, please choose which library you would like to acess ")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if answer == "1":

        email = input("Welcome to The School Library, enter your email ")
        userindex = 0
        for i in range(len(users)):
            if users[i].Email == email:  # checking their email inorder to check which class they are from
                x = users[i].__class__.__name__  # assigning x to the type of user found
                userindex = i  # checking the location of the user in the list of different users
                tempuser = users[userindex]



        if x == "NormalUser":  # if the system identifies them as normal user, their options are set for them to choose their next action
            print("Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period")
            option = input("What would you like to do? ")
            if option == "1":  # borrowing a book
                Book_Borrowed = input("What book would you like to borrow? ")
                if tempuser.SearchBook(Book_Borrowed):
                    for i in range(len(booklist)):
                        if booklist[i].Title == Book_Borrowed:  # searching for the book title in the list of books to check if available
                            users[userindex].BorrowBook(booklist[i])
                            print(booklist[i].NoCopiesBorrowed)
                            print("Done! :)")
                            break
                        else:
                            print("sorry book not available right now :(")
                            break
                else:
                    print("sorry book not available right now :(")



            elif option == "2":  # book being returned
                Book_Returned = input("what book would you like to return? ")
                if users[userindex].SearchBook(Book_Returned):
                    for i in range(len(booklist)):
                        if booklist[i].Title == Book_Returned:  # checking if the book name being returned is equal to the book borrowed from user
                            users[userindex].ReturnBook(booklist[i])
                            print(booklist[i].NoCopiesBorrowed)
                            print("Done! :)")
                        else:
                            print("sorry, book not found :(")

            elif option == "3":  # searching for a book
                Book_Search = input("what book you like to search for? ")
                if users[userindex].SearchBook(Book_Search):
                    print("Book has been found :)")
                else:
                    print("Book has not been found :(")

            elif option == "4":
                extendloan = input("what book would you like to extend its loan? ")
                Book_Extension = input("how many days for extension? ")
                int_BookExtention = int(
                    Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                for i in range(len(Book.booklist)):  # checking the length of the book list
                    if Book.booklist[i].Title == extendloan:  # finding it by the book's title
                        users[userindex].ExtendLoan(int_BookExtention, Book.booklist[
                            i])  # adding the number of days wanted to extend to the already set extended loan
                        print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")
                    else:
                        print("Error, try again")


        elif x == "Librarian":  # if the system identifies them as librarian, their options are set for them to choose their next action
            print(
                "Options are 1)add book to system, 2)remove book from system, 3)search book, 4)extend loan period for a borrowed book")
            option = input("What would you like to do? ")
            if option == "1":  # adding book to system
                Add_Book = input("Please input data of the book in this format book[title,author,ISBN,Total copies,Online,Borrower info]")
                Add_Book = Add_Book.split(",")
                tempbook = Book(Add_Book[0], Add_Book[1], int(Add_Book[2]), int(Add_Book[3]), Add_Book[4], Add_Book[5])
                booklist.append(tempbook)  # adding the new book to book list
                print(booklist)

            elif option == "2":  # removing book from system
                Remove_Book = input("Enter book name")
                for i in Book.booklist:
                    if Remove_Book == i.Title:  # searching for book using title
                        Book.booklist.pop(Book.booklist.index(i))  # removing or "popping" from book list
                        print("Book has been removed")
                        break
                else:
                    print("Book not found :(")


            elif option == "3":  # searching for book
                Book_Search = input("What book are you searching for? ")
                if users[userindex].SearchBook(Book_Search):  # searching for the book
                    print("Book Found")
                else:
                    print("Sorry, book not found :(")

            elif option == "4":  # extend loan for book
                Extend_Loan = input("what book? ")
                Book_Extension = input("how many days? ")
                int_BookExtension = int(
                    Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                for i in range(len(Book.booklist)):  # checking the length of the book list
                    if Book.booklist[i].Title == Extend_Loan:  # finding it by the book's title
                        users[userindex].ExtendLoan(int_BookExtension, Book.booklist[
                            i])  # adding the number of days wanted to extend to the already set extended loan
                        print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")


        elif x == "SystemDomain":  # if the system identifies them as system domain, their options are set for them to choose their next action
            print("options are 1)add user, 2)remove user")
            option = input("what would you like to do? ")
            if option == "1":  # adding user to system
                type_user = input("please enter type of user 1)NormalUser, 2)Librarian, 3)SystemDomain, 4)Student")
                if type_user == "1":
                    # who = "NormalUser"
                    userinfoFull = input("enter full info in this format: name, id, email, type, Area, Age, credit_card, security_number")
                    userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                    School_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                    users.append(NormalUser(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],userinfoFull[4],userinfoFull[5], userinfoFull[6],userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                    print("User has been added sucessfully :)")

                elif type_user == "2":  # process is repeated twice after, once for Librarian class and one for System Domian
                    userinfoFull = input("enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                    userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                    School_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                    users.append(Librarian(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],userinfoFull[4], userinfoFull[5], userinfoFull[6],userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                    print("User has been added sucessfully :)")


                elif type_user == "3":
                    userinfoFull = input(
                        "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                    userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                    School_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                            userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                    users.append(
                        SystemDomain(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                   userinfoFull[4], userinfoFull[5], userinfoFull[6],
                                   userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                    print("User has been added sucessfully :)")

                elif type_user == "4": #if adding student
                    userinfoFull = input("enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                    userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                    School_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                            userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                    users.append(Student(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                   userinfoFull[4], userinfoFull[5], userinfoFull[6],userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                    print("User has been added sucessfully :)")


            elif option == "2":  # removing user
                emailsearch = input("please enter user's email ")
                for i in users:
                    if emailsearch == i.Email:  # looking for the user by email
                        users.pop(users.index(i))  # removing or "popping" the user found by the given email found
                        print("done bestie!!!!!!!!!!!!!")
                        break
                    else:
                        print("user not found :(")
        elif x == "Student":
            print("Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period")
            option = input("What would you like to do? ")
            if option == "1":  # borrowing a book
                #ask about this!!!!!
                Book_Borrowed = input("What book would you like to borrow, enter book,user? ")
                book_borrowed=Book_Borrowed.split(",")
                School_Library.borrow_book(book_borrowed[0],book_borrowed[1])

            elif option == "2":  # book being returned
                Book_Returned = input("what book would you like to return? ")
                if users[userindex].SearchBook(Book_Returned):
                    for i in range(len(Book.booklist)):
                        if Book.booklist[
                            i].Title == Book_Returned:  # checking if the book name being returned is equal to the book borrowed from user
                            users[userindex].ReturnBook(Book.booklist[i])
                            print(Book.booklist[i].NoCopiesBorrowed)
                            print("Done! :)")
                        else:
                            print("sorry, book not found :(")

            elif option == "3":  # searching for a book
                Book_Search = input("what book you like to search for? ")
                if users[userindex].SearchBook(Book_Search):
                    print("Book has been found :)")
                else:
                    print("Book has not been found :(")

            elif option == "4":
                extendloan = input("what book would you like to extend its loan? ")
                Book_Extension = input("how many days for extension? ")
                int_BookExtention = int(
                    Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                for i in range(len(Book.booklist)):  # checking the length of the book list
                    if Book.booklist[i].Title == extendloan:  # finding it by the book's title
                        users[userindex].ExtendLoan(int_BookExtention, Book.booklist[
                            i])  # adding the number of days wanted to extend to the already set extended loan
                        print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")
                    else:
                        print("Error, try again")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Minucipal Library
    elif answer=="2":
        email = input("Welcome to Municipal Library,Please enter your email ")
        userindex = 0
        for i in range(len(users)):
            if users[i].Email == email:  # checking their email inorder to check which class they are from
                x = users[i].__class__.__name__  # assigning x to the type of user found
                userindex = i  # checking the location of the user in the list of different users
                tempuser = users[userindex]

                if x == "NormalUser":  # if the system identifies them as normal user, their options are set for them to choose their next action
                    print("Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period")
                    option = input("What would you like to do? ")
                    if option == "1":  # borrowing a book
                        Book_Borrowed = input("What book would you like to borrow? ")
                        if tempuser.SearchBook(Book_Borrowed):
                            for i in range(len(Book.booklist)):
                                if Book.booklist[
                                    i].Title == Book_Borrowed:  # searching for the book title in the list of books to check if available
                                    users[userindex].BorrowBook(Book.booklist[i])
                                    print(Book.booklist[i].NoCopiesBorrowed)
                                    print("Done! :)")
                                else:
                                    print("sorry book not available right now :(")

                    elif option == "2":  # book being returned
                        Book_Returned = input("what book would you like to return? ")
                        if users[userindex].SearchBook(Book_Returned):
                            for i in range(len(Book.booklist)):
                                if Book.booklist[
                                    i].Title == Book_Returned:  # checking if the book name being returned is equal to the book borrowed from user
                                    users[userindex].ReturnBook(Book.booklist[i])
                                    print(Book.booklist[i].NoCopiesBorrowed)
                                    print("Done! :)")
                                else:
                                    print("sorry, book not found :(")

                    elif option == "3":  # searching for a book
                        Book_Search = input("what book you like to search for? ")
                        if users[userindex].SearchBook(Book_Search):
                            print("Book has been found :)")
                        else:
                            print("Book has not been found :(")

                    elif option == "4":
                        extendloan = input("what book would you like to extend its loan? ")
                        Book_Extension = input("how many days for extension? ")
                        int_BookExtention = int(
                            Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                        for i in range(len(Book.booklist)):  # checking the length of the book list
                            if Book.booklist[i].Title == extendloan:  # finding it by the book's title
                                users[userindex].ExtendLoan(int_BookExtention, Book.booklist[
                                    i])  # adding the number of days wanted to extend to the already set extended loan
                                print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")
                            else:
                                print("Error, try again")


                elif x == "Librarian":  # if the system identifies them as librarian, their options are set for them to choose their next action
                    print(
                        "Options are 1)add book to system, 2)remove book from system, 3)search book, 4)extend loan period for a borrowed book")
                    option = input("What would you like to do? ")
                    if option == "1":  # adding book to system
                        Add_Book = input("Please input data of the book in this format book[title,author,ISBN,Online,Borrower info]")
                        Book.booklist.append(Add_Book)  # adding the new book to book list
                        print(Book.booklist)

                    elif option == "2":  # removing book from system
                        Remove_Book = input("Enter book name")
                        for i in Book.booklist:
                            if Remove_Book == i.Title:  # searching for book using title
                                Book.booklist.pop(Book.booklist.index(i))  # removing or "popping" from book list
                                print("Book has been removed")
                                break
                        else:
                            print("Book not found :(")


                    elif option == "3":  # searching for book
                        Book_Search = input("What book are you searching for? ")
                        if users[userindex].SearchBook(Book_Search):  # searching for the book
                            print("Book Found")
                        else:
                            print("Sorry, book not found :(")

                    elif option == "4":  # extend loan for book
                        Extend_Loan = input("what book? ")
                        Book_Extension = input("how many days? ")
                        int_BookExtension = int(
                            Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                        for i in range(len(Book.booklist)):  # checking the length of the book list
                            if Book.booklist[i].Title == Extend_Loan:  # finding it by the book's title
                                users[userindex].ExtendLoan(int_BookExtension, Book.booklist[
                                    i])  # adding the number of days wanted to extend to the already set extended loan
                                print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")


                elif x == "SystemDomain":  # if the system identifies them as system domain, their options are set for them to choose their next action
                    print("options are 1)add user, 2)remove user")
                    option = input("what would you like to do? ")
                    if option == "1":  # adding user to system
                        type_user = input("please enter type of user 1)NormalUser, 2)Librarian, 3)SystemDomain ")
                        if type_user == "1":
                            # who = "NormalUser"
                            userinfoFull = input("enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            Municipal_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],userinfoFull[4],userinfoFull[5],userinfoFull[6],userinfoFull[7])
                            users.append(NormalUser(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],userinfoFull[4],userinfoFull[5],userinfoFull[6],userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")

                        elif type_user == "2":  # process is repeated twice after, once for Librarian class and one for System Domian
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            Municipal_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                                       userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                            users.append(
                                Librarian(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3], userinfoFull[4],
                                           userinfoFull[5], userinfoFull[6],
                                           userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")

                        elif type_user == "3":
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            Municipal_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                                       userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                            users.append(
                                SystemDomain(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3], userinfoFull[4],
                                           userinfoFull[5], userinfoFull[6],
                                           userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")

                        elif type_user == "4":
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            Municipal_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                                       userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                            users.append(
                                Student(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                             userinfoFull[4],
                                             userinfoFull[5], userinfoFull[6],
                                             userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")


                    elif option == "2":  # removing user
                        emailsearch = input("please enter user's email ")
                        for i in users:
                            if emailsearch == i.Email:  # looking for the user by email
                                users.pop(users.index(i))  # removing or "popping" the user found by the given email found
                                print("done!!!!!!!!!!!!!")
                                break
                            else:
                                print("user not found :(")


                elif x == "Student":
                    print("Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period")
                    option = input("What would you like to do? ")
                    if option == "1":  # borrowing a book
                        # ask about this!!!!!
                        Book_Borrowed = input("What book would you like to borrow, enter book,user? ")
                        book_borrowed = Book_Borrowed.split(",")
                        Municipal_Library.borrow_book(book_borrowed[0], book_borrowed[1])

                    elif option == "2":  # book being returned
                        Book_Returned = input("what book would you like to return? ")
                        if users[userindex].SearchBook(Book_Returned):
                            for i in range(len(Book.booklist)):
                                if Book.booklist[
                                    i].Title == Book_Returned:  # checking if the book name being returned is equal to the book borrowed from user
                                    users[userindex].ReturnBook(Book.booklist[i])
                                    print(Book.booklist[i].NoCopiesBorrowed)
                                    print("Done! :)")
                                else:
                                    print("sorry, book not found :(")

                    elif option == "3":  # searching for a book
                        Book_Search = input("what book you like to search for? ")
                        if users[userindex].SearchBook(Book_Search):
                            print("Book has been found :)")
                        else:
                            print("Book has not been found :(")

                    elif option == "4":
                        extendloan = input("what book would you like to extend its loan? ")
                        Book_Extension = input("how many days for extension? ")
                        int_BookExtention = int(
                            Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                        for i in range(len(Book.booklist)):  # checking the length of the book list
                            if Book.booklist[i].Title == extendloan:  # finding it by the book's title
                                users[userindex].ExtendLoan(int_BookExtention, Book.booklist[
                                    i])  # adding the number of days wanted to extend to the already set extended loan
                                print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")
                            else:
                                print("Error, try again")


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #National Library
    elif answer == "3":
        email = input("Welcome to Municipal Library,Please enter your email ")
        userindex = 0
        for i in range(len(users)):
            if users[i].Email == email:  # checking their email inorder to check which class they are from
                x = users[i].__class__.__name__  # assigning x to the type of user found
                userindex = i  # checking the location of the user in the list of different users
                tempuser = users[userindex]

                if x == "NormalUser":  # if the system identifies them as normal user, their options are set for them to choose their next action
                    print("Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period")
                    option = input("What would you like to do? ")
                    if option == "1":  # borrowing a book
                        Book_Borrowed = input("What book would you like to borrow? ")
                        if tempuser.SearchBook(Book_Borrowed):
                            for i in range(len(Book.booklist)):
                                if Book.booklist[
                                    i].Title == Book_Borrowed:  # searching for the book title in the list of books to check if available
                                    users[userindex].BorrowBook(Book.booklist[i])
                                    print(Book.booklist[i].NoCopiesBorrowed)
                                    print("Done! :)")
                                else:
                                    print("sorry book not available right now :(")

                    elif option == "2":  # book being returned
                        Book_Returned = input("what book would you like to return? ")
                        if users[userindex].SearchBook(Book_Returned):
                            for i in range(len(Book.booklist)):
                                if Book.booklist[
                                    i].Title == Book_Returned:  # checking if the book name being returned is equal to the book borrowed from user
                                    users[userindex].ReturnBook(Book.booklist[i])
                                    print(Book.booklist[i].NoCopiesBorrowed)
                                    print("Done! :)")
                                else:
                                    print("sorry, book not found :(")

                    elif option == "3":  # searching for a book
                        Book_Search = input("what book you like to search for? ")
                        if users[userindex].SearchBook(Book_Search):
                            print("Book has been found :)")
                        else:
                            print("Book has not been found :(")

                    elif option == "4":
                        extendloan = input("what book would you like to extend its loan? ")
                        Book_Extension = input("how many days for extension? ")
                        int_BookExtention = int(
                            Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                        for i in range(len(Book.booklist)):  # checking the length of the book list
                            if Book.booklist[i].Title == extendloan:  # finding it by the book's title
                                users[userindex].ExtendLoan(int_BookExtention, Book.booklist[
                                    i])  # adding the number of days wanted to extend to the already set extended loan
                                print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")
                            else:
                                print("Error, try again")


                elif x == "Librarian":  # if the system identifies them as librarian, their options are set for them to choose their next action
                    print(
                        "Options are 1)add book to system, 2)remove book from system, 3)search book, 4)extend loan period for a borrowed book")
                    option = input("What would you like to do? ")
                    if option == "1":  # adding book to system
                        Add_Book = input(
                            "Please input data of the book in this format book[title,author,ISBN,Online,Borrower info]")
                        Book.booklist.append(Add_Book)  # adding the new book to book list
                        print(Book.booklist)

                    elif option == "2":  # removing book from system
                        Remove_Book = input("Enter book name")
                        for i in Book.booklist:
                            if Remove_Book == i.Title:  # searching for book using title
                                Book.booklist.pop(Book.booklist.index(i))  # removing or "popping" from book list
                                print("Book has been removed")
                                break
                        else:
                            print("Book not found :(")


                    elif option == "3":  # searching for book
                        Book_Search = input("What book are you searching for? ")
                        if users[userindex].SearchBook(Book_Search):  # searching for the book
                            print("Book Found")
                        else:
                            print("Sorry, book not found :(")

                    elif option == "4":  # extend loan for book
                        Extend_Loan = input("what book? ")
                        Book_Extension = input("how many days? ")
                        int_BookExtension = int(
                            Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                        for i in range(len(Book.booklist)):  # checking the length of the book list
                            if Book.booklist[i].Title == Extend_Loan:  # finding it by the book's title
                                users[userindex].ExtendLoan(int_BookExtension, Book.booklist[
                                    i])  # adding the number of days wanted to extend to the already set extended loan
                                print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")


                elif x == "SystemDomain":  # if the system identifies them as system domain, their options are set for them to choose their next action
                    print("options are 1)add user, 2)remove user")
                    option = input("what would you like to do? ")
                    if option == "1":  # adding user to system
                        type_user = input("please enter type of user 1)NormalUser, 2)Librarian, 3)SystemDomain ")
                        if type_user == "1":
                            # who = "NormalUser"
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            National_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2],
                                                       userinfoFull[3], userinfoFull[4], userinfoFull[5], userinfoFull[6],
                                                       userinfoFull[7])
                            users.append(NormalUser(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                                    userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[
                                                        7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")

                        elif type_user == "2":  # process is repeated twice after, once for Librarian class and one for System Domian
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            National_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2],
                                                       userinfoFull[3],
                                                       userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                            users.append(
                                Librarian(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                          userinfoFull[4],
                                          userinfoFull[5], userinfoFull[6],
                                          userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")

                        elif type_user == "3":
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            National_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2],
                                                       userinfoFull[3],
                                                       userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                            users.append(
                                SystemDomain(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                             userinfoFull[4],
                                             userinfoFull[5], userinfoFull[6],
                                             userinfoFull[
                                                 7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")

                        elif type_user == "4":
                            userinfoFull = input(
                                "enter full info in this format: name,id,user_type,email,age,credit_card,security_number,Area")
                            userinfoFull = userinfoFull.split(",")  # spliting the input of the user by ","
                            National_Library.add_user(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2],
                                                       userinfoFull[3],
                                                       userinfoFull[4], userinfoFull[5], userinfoFull[6], userinfoFull[7])
                            users.append(
                                Student(userinfoFull[0], int(userinfoFull[1]), userinfoFull[2], userinfoFull[3],
                                        userinfoFull[4],
                                        userinfoFull[5], userinfoFull[6],
                                        userinfoFull[7]))  # adding the variables inputed by user in by in certain indexes
                            print("User has been added sucessfully :)")


                    elif option == "2":  # removing user
                        emailsearch = input("please enter user's email ")
                        for i in users:
                            if emailsearch == i.Email:  # looking for the user by email
                                users.pop(users.index(i))  # removing or "popping" the user found by the given email found
                                print("done!!!!!!!!!!!!!")
                                break
                            else:
                                print("user not found :(")


                elif x == "Student":
                    print("Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period")
                    option = input("What would you like to do? ")
                    if option == "1":  # borrowing a book
                        # ask about this!!!!!
                        Book_Borrowed = input("What book would you like to borrow, enter book,user? ")
                        book_borrowed = Book_Borrowed.split(",")
                        National_Library.borrow_book(book_borrowed[0], book_borrowed[1])

                    elif option == "2":  # book being returned
                        Book_Returned = input("what book would you like to return? ")
                        if users[userindex].SearchBook(Book_Returned):
                            for i in range(len(Book.booklist)):
                                if Book.booklist[
                                    i].Title == Book_Returned:  # checking if the book name being returned is equal to the book borrowed from user
                                    users[userindex].ReturnBook(Book.booklist[i])
                                    print(Book.booklist[i].NoCopiesBorrowed)
                                    print("Done! :)")
                                else:
                                    print("sorry, book not found :(")

                    elif option == "3":  # searching for a book
                        Book_Search = input("what book you like to search for? ")
                        if users[userindex].SearchBook(Book_Search):
                            print("Book has been found :)")
                        else:
                            print("Book has not been found :(")

                    elif option == "4":
                        extendloan = input("what book would you like to extend its loan? ")
                        Book_Extension = input("how many days for extension? ")
                        int_BookExtention = int(
                            Book_Extension)  # turning it to an integer to add it to the usual loan period already set
                        for i in range(len(Book.booklist)):  # checking the length of the book list
                            if Book.booklist[i].Title == extendloan:  # finding it by the book's title
                                users[userindex].ExtendLoan(int_BookExtention, Book.booklist[
                                    i])  # adding the number of days wanted to extend to the already set extended loan
                                print("loan extendend to " + Book.booklist[i].LoanPeriod + "days")
                            else:
                                print("Error, try again")

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
except KeyboardInterrupt:
    save()
    quit()