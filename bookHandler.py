import time
from  fileHandler import createNewBook, readallbooks, delBookFromFile, updateBook, searchBook
from re import match


#check if the input is valid or not
def askForValidStr(message):
    value = input(message)
    check = match('^[A-Za-z]', value)
    if check:
        return value
        
    else:
        print("---------- Enter a correct string ---------- ")
        return askForValidStr(message)

def askForValidInt(message):
    value = input(message)
    check = match('[0-9]{4}', value)
    if value.isnumeric() and check:
        return value
    else:
        print("---------- Enter a correct integer number ---------- ")
        return askForValidInt(message)
    
def askForValidNum(message):
    value = input(message)
    if value.isnumeric():
        return value
    else:
        print("---------- Enter a correct integer number ---------- ")
        return askForValidInt(message)



def basicInfo():
    tittle = askForValidStr("Please enter the tittle: ")
    description = askForValidStr("Please enter the description: ")
    year = askForValidInt("Please enter the year of publication: ")

    return tittle , description , year



def createBook():
    print("--------- create book --------")
    book_details = basicInfo()
    book_id = time.time()
    # book_details = list(book_details)
    book_id = str(round(time.time()))
    book_info = f"{book_id}:{book_details[0]}:{book_details[1]}:{book_details[2]}\n"
    added = createNewBook(book_info)
    if added:
        print("-------- New Book Created --------")


def listallbooks():
    books = readallbooks()
    print("-------- Books --------")
    print(books)

def deleteBook():

    listallbooks()

    book_id = askForValidNum("Enter the book id what you want to delete: ")

    # search all books that contains this id
    deleted = delBookFromFile(book_id)

    #check i fthe boo is exist
    if deleted:
        print("----- Book deleted successfully -----")
        print(" ")
        print("-----------------------------------------------------")
        listallbooks()
    # delete the book

    else:
        return deleteBook()


def editBook():

    listallbooks()
    book_id = askForValidNum("Enter the book id what you want to edit: ")
    book_index = searchBook(book_id)

    if book_index or book_index==0:
        print("------ edit the book info -----")
        book_data = basicInfo()
        update_book = f'{book_id}:{book_data[0]}:{book_data[1]}:{book_data[2]}\n'
        #send this data to the file
        updated = updateBook(book_index, update_book)

        if updated:
            print("----- Updated Successfully ------")

    else:
        return editBook()