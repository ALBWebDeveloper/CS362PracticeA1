

def conversion(convertChar):
    print("This program outputs the ascii value of a number you enter\n")
    #value = input("Enter a character:  ")

    if type(convertChar) == int:
     raise TypeError("only character")
     exit(-1)
    
    result = ord(convertChar)
    
    print("The ascii value of {} is {}".format(convertChar, result))
    print("\nEnd of program")
    return result

#conversion('*')
#onversion(9)