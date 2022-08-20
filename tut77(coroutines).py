# coroutines -- are used to run any function from in between

def searcher():      #   here searcher will act as coroutines
    import time
    #some 4 secc time consuming task
    book = " This is a book in harry and codewithharry "
    time.sleep(4)
    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
search= searcher()
next(search)
search.send("harry")
input("Press any key")
search.send("harry and")

search.close()
# input("Press any key")
# search.send("This is")
# input("Press any key")
# search.send("codewithharry")
# input("Press any key")
# search.send("book")

