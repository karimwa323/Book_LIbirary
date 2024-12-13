
"""

    libirary ---> books
    file ---> all book informations
    book tittle, decription, year, id

    ---> console application
    ===> CRUD operation onthre book 
    creatae
    list, update, delete

"""



from bookHandler import createBook, listallbooks, deleteBook, editBook



def mainMenu():
    option = input("""
create ---> c
list   ---> l
edit   ---> e
delete ---> d
whats your choise : """)
    
    while(True):
        if option in ["c" , "l" , "e" , "d"]:
            if option == 'c':
                createBook()
                break
            elif option == 'e':
                editBook()
                break
            elif option == 'd':
                deleteBook()
                break
            else:
                listallbooks()
                break
        else:
            print("""
Please enter a valid option...
                """)
            break
    return mainMenu()


mainMenu()