def func():
    
    while True:
        try:
            n = int(input("Enter no: "))
        
        except:
            print("Please try again")
            continue
        else:
            break
    print("The number square is")
    print(n**2)

func()
