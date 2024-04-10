Quick description of the whole Library system


>>First Class Book
the class has a list f all the books in all the libraries, containing all the requirements of books data 
(title,autho,isbn,total copies, online copy(if availabele),and borrowers info)
includig fuctions to retireve every attribute in thems as well as borrowing and returning a book and searching for a book.


>>Second Class User
the class includes all the info of a user such as name, id, the nbooks they borrowed, email, age, credit card, social security, area.
with all their setters and getters
 
	>>the first sub-class Normal user
inherits all their attributes from the class parent User and all its functions.
adds a new fucntion to extend a users loan for a book

	>>the second sub-class Librarian 
inherits all their attributes from the class parent User and the function search book

	>>the third sub-class System Domain
inherits all their attributes from the class parent User and the function search book
fuction add user to the users list and remove user from user list

	>>the fourth sub-class Student
inherits all their attributes from the class parent User


>>Thrid Class Library
includes the attributes library name, library type, user type, a list ofusers, list ofbooks in library, list of active loans, borrow policy
with all their setters and getters
fuctions include adding a user, remove a user, add a book, remove a book, return a book, return a book, search a book

	>>first sub-class School library
inherits all their attributes from the class parent User and the function add user and borrow book

	>>second sub-class Municipal Library
inherits all their attributes from the class parent User and the function add user and borrow book

	>>third sub class National Library
inherits all their attributes from the class parent User and the function add user and borrow book


Main System
>>the system asks the user which library they want to access, 1-School 2-Municipal 3-National
>>user then enters their email and autuomatically the system checks in the list of users which user type they are
	>>if they are a Normal user, they have a list of options to choose from,Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period
	>>if they are Librarian user they have a list of options to choose from, Options are 1)add book to system, 2)remove book from system, 3)search book, 4)extend loan period for a borrowed book
	>>if they are System Domain they have a list of options to choose from,options are 1)add user, 2)remove user
	>>if they are Student they have a list of options to choose from,Options are 1)Borrow a book , 2)return book , 3)search book, 4)extend period

the add user function and borrow book are differen in each library
if they are in School Library then:
	>>add user checks the type of user being added first before adding them
	>>borrow book checks that the student borrwing the book is not restricted and the user type is a student

if they are Municipal Library then:
	>>add user checks if the user is in the area before adding them
	>>borrow book checks to see in the user has a credit card, if not they are not allowed to borrow book

if they are National library:
	>>add user checks if they have a social security number before adding them, if not then they are not added in the system
	>>borrow book checks to see in the user has a credit card, if not they are not allowed to borrow book
