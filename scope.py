# global scope
sentence = "Hello World (Global Scope)"

def say_hello(): # global scope
    # local scope
    sentence = "Hello World (Local Scope)"
   
    print(sentence + " inside main function")

    def say_hello_again(): # local scope
        print(sentence + " inside child function")

    say_hello_again()


say_hello()

# say_hello_again () you can't use this function because of local scope


