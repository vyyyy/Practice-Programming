import urllib.request

def read_text():
    #open the file
    quotes = open("/Users/vypatz/Desktop/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    #check the file
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("Could not scan the document")
    
read_text()

'''The open function (called on the filepath and stored in the variable quotes)
instantiates an object called quotes of type File.
This is how you know you have to call methods on that object. e.g.
calling the read function on quotes.
calling the read function on connection (urlopen also instantiates connection
as an object by calling the __init__ function behind the scenes.).
This is what allows you to do things with/to the object'''
