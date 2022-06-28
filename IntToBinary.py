
def BinaryToInt():
    #binary string in acneding order (1,2,4,8,16)
    binary_string = str(input("give a binary string: "))
    sum = 0
    mult = 0
    for char in binary_string:
        if char == "1":
            sum += pow(2,mult)
        mult += 1
    print(sum)

def IntToBinary():
    #binary is true when num % 2 == 1, true == 1

    num = int(input("give num: "))
    binary_string = ""
    while(num != 0):
        if num % 2 == 1:
            binary_string += "1"
        else:
            binary_string += "0"
        num = num//2;#integer division is "//" in python, "/" is float division
        #print(num)
    print(binary_string)

def Continue():
    userCont = input("Do you want to continue: ")
    if userCont == "y" or userCont == "yes":
        return True
    else:
        return False

#main
print("this is ascending order binary format")
game_loop = True
while (game_loop):
    user_use = input("Do you want to make BinaryToInt('1') or IntToBinary('2'): ")
    user_loop = int(input("How many times(int): "))

    if user_use == "1":
        while user_loop != 0:
            user_loop -= 1
            BinaryToInt()
    if user_use == "2":
        while user_loop != 0:
            user_loop -= 1
            IntToBinary()

    game_loop = Continue()
