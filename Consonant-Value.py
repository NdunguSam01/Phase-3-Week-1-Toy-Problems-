#Defining a function that will calculate the consonant value

def consonant_value_calculator(string):

    #Declaring variables that stores the vowels, maximum value and current value
    vowels="aeiou"
    maximum_value=0
    current_value=0

    #Checking if a character in the passed string is a vowel and returning only the characters that are not 
    for character in string:
        if character not in vowels:

            #Using the ord() function to calculate the value of the character for the starting character (a)
                #ord() returns the number representing the unicode code of a specified character
            value=ord(character) - ord("a") + 1

            #Updating the current value variable to equal the calculated value
            current_value += value
        
        #Resetting the value of current value variable to 0 once a vowel is encountered
        else:
            current_value = 0
        
        #Checking if the current value is greater than the value currently stored in the maximum value variable and updating it if the current value is greater
        if current_value > maximum_value:
            maximum_value = current_value
        
    print(maximum_value)

consonant_value_calculator("strength")