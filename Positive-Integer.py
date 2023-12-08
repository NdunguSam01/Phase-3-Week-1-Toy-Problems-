#Defining a function that takes in three arguments: a, b, and c

def positive_integer(a, b, c):

    #Initializing a variable that will store the number of positive integers
    total_positive_integers=0

    #Creating and if statement that checks if the passed in arguments are positive integers

    if a > 0:
        #Updating the number of positive integers if the condition is met
        total_positive_integers += 1
    if b > 0:
        total_positive_integers += 1
    if c > 0:
        total_positive_integers += 1


    print(True) if total_positive_integers == 2 else print(False)

positive_integer(2, 4, -3)
positive_integer(-4, 6, 8)
positive_integer(4, -6, 9)
positive_integer(-4, 6, 0)
positive_integer(4, 6, 10)
positive_integer(-14, -3, -4) 