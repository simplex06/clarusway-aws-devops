def drawbox():
    a = int(input("Please enter the side length of the box: "))
    for i in range(a):
        if i == 0 or i == a-1:
            print(a*"#")
        else:
            print("#" + " "*(a-2) + "#")

drawbox()