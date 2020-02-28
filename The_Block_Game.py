for i in range(int(input())):
    n = input()
    rev = n[::-1]
    if n == rev :
        print("wins")
    else:
        print("losses")

