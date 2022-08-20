# create a librabry class
#     display book
#     lend book
#     add book
#     return book
# harrylibrary = Library( list of books, library name )
# dictionary -------- which book is lended to which person
#  key = book , value = nameofperson
#  create  main function and run an infinite
#  while loop asking users for their input
# --------------------------------------------solution-----------------------------------------------
class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.Lenddict = {}
    def displaybooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)
    def lendbook(self, user, book):
        if book not in self.Lenddict.keys():
            self.Lenddict.update({book:user})
            print("Lender-Book Database has been updated")
        else:
            print(f"The Book is already being used by {self.Lenddict[book]}")
    def addbook(self,book):
        self.booklist.append(book)
        print("Book has been added")
    def returnbook(self,book):
        self.Lenddict.pop(book)
        print("Book has been returned")
if __name__ == '__main__':
    akash = Library(["Python","Rich Dad Poor Dad","The Richest Man in Babylon","C++",
                     "Secret","Power of Subconscious Mind"],"The-Knowledge")
    while(True):
        print(f"Welcome to the {akash.name} library")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add Books")
        print("4. Return Books")
        user_choise = input()
        if user_choise not in ["1","2","3","4"]:
            print("Please enter a valid option")
            continue
        else:
            user_choise = int(user_choise)

        if user_choise == 1:
            akash.displaybooks()
        elif user_choise ==2:
            book = input("Enter the book you want to lend:")
            user = input("Enter your name:")
            akash.lendbook(user,book)
        elif user_choise ==3:
            book = input("Enter the book you want to add:")
            akash.addbook(book)
        elif user_choise ==4:
            book = input("Enter the book you want to return:")
            akash.returnbook(book)
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        user_choise2 = ""
        while(user_choise2!="c" and user_choise2!="q"):
            user_choise2 = input()
            if user_choise2 == "q":
                exit()
            if user_choise2 == "c":
                continue