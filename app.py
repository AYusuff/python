from Library.math import *
keep_working = True

while keep_working:
    a = int(input ("provide the first value: "  ))
    b = int(input ("provide the second value: " ))
    print("What operation do you want to perform?")
    operation = input("1.(+) 2.(-) 3.(*) 4.(/): "  )
    if operation == '1':
        print(sum(a,b))
    elif operation == '2':
        print(subt(a,b))
    elif operation == '3':
        print(mult(a,b))
    else:
        print(div(a,b))
    print("Would you like to perform another operation?:")
    proceed = input( "1. (Y) 2. (n)")
    if proceed == '1' :
        keep_working = True
    else:
        keep_working = False

