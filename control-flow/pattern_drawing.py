size = int(input("Enter the size of the pattern: "))
row = 0
column = 0
while row < size:
    for row in range(size):
        for column in range(size):
            print("*", end="")
            column += 1
        print()
        row += 1