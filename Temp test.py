# temperature conversion

print("Convert your temperature from C to F or C to F!")

def repeatfunc():
    repeat = input("Would you like to convert another? ").lower()
    if repeat == "no":
        print("Thanks, love you")
    elif repeat == 'yes':
        print("Yeyyyyyy fun fun fun")
        conversion()
    else:
        print("stop that" )

def conversion():
    which = input("Is your temperature C or F? ").lower()
    value = int(input("What is its value? "))
    if which == 'c':
        result = value * 9 / 5 + 32
        print(result, "is your temperature in F")
        repeatfunc()
          #"is your temperature in F") 
    elif which == 'f':
        result = (value - 32) * 5 / 9
        print(result, "is your temperature in C")
 #         "is your temperature in C")
        repeatfunc()
    else:
        result = 'Please enter C or F'    

conversion()
    
    
