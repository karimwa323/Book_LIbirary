

def writeAllBooks(books):
    try:
        fileobject = open("books.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        fileobject.writelines(books)
        return True

def createNewBook(book):
    try:
        fileobject = open("books.txt", "a")
    except Exception as e:
        print(e)
        return False
    else:
        fileobject.write(book)
        return True


def readallbooks():
    try:
        fileobject = open("books.txt", "r")
    except Exception as e:
        print(e)
        return False
    else:
        books = fileobject.readlines()
        # books = str(books)
        return books


def searchBook(book_id):
    #check if the book is exist in the file
    books = readallbooks()
    books = books
    for book in books:
        book_details = book.split(":")
        if book_details[0] == str(book_id):
            book_index = books.index(book)
            print(book_index)
            return book_index
    else:
        print("error")        

def delBookFromFile(book_id):
    book_index = searchBook(book_id)
    if book_id:
        allbooks = readallbooks()
        del allbooks[book_index]

    # write the new list to the file
    deleted = writeAllBooks(allbooks)
    return deleted


def updateBook(book_index, book_data):

    allbooks = readallbooks()
    allbooks[book_index] = book_data
    updated = writeAllBooks(allbooks)
    return updated