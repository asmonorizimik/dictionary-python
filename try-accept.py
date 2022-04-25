print("1. Squares")
print("2. Cubes")
try:
    ch_1 = int(input("Enter Your Choice (1 or 2): "))
    if ch_1==1:
        print("\n1. Squares of First 5 Even Natural Numbers")
        print("2. Squares of First 5 Odd Natural Numbers")
        try:
            ch_2 = int(input("Enter Your Choice (1 or 2): "))
            if ch_2==1:
                squares = {n: n*n for n in range(1, 11) if n%2==0}
                print("\n", squares, sep="")
            elif ch_2==2:
                squares = {n: n*n for n in range(1, 11) if n%2!=0}
                print("\n", squares, sep="")
        except ValueError:
            print("\nInvalid Input!")
    elif ch_1==2:
        print("\n1. Cubes of First 5 Even Natural Numbers")
        print("2. Cubes of First 5 Odd Natural Numbers")
        try:
            ch_2 = int(input("Enter Your Choice (1 or 2): "))
            if ch_2==1:
                cubes = {n: n*n*n for n in range(1, 11) if n%2==0}
                print("\n", cubes, sep="")
            elif ch_2==2:
                cubes = {n: n*n*n for n in range(1, 11) if n%2!=0}
                print("\n", cubes, sep="")
        except ValueError:
            print("\nInvalid Input!")
except ValueError:
    print("\nInvalid Input!")