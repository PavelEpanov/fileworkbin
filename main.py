def main():
    get_user_numbers()
    read_numbers()


def get_user_numbers():

    myfile = open("filesquared.txt", "w")

    number = int(input("Введите число: "))
    number = bin(number)
    myfile.write(str(number) + " ")

    meta = int(input("'1' - Ввести еще число, '2' - закончить ввод: "))
    if meta == 2:
        meta = ""
    elif meta == 1:
        number = int(input("Ввести число ещё:"))

    while meta != "":
        number = bin(number)
        myfile.write(str(number) + " ")
        meta = int(input("'1' - Ввести еще число, '2' - закончить ввод: "))
        if meta == 2:
            meta = ""
        elif meta == 1:
            number = int(input("Ввести число ещё:"))

    #myfile.write("a" + " ")

    myfile.close()

def read_numbers():
    myfile = open("filesquared.txt", "r")

    list = []

    string = ""

    a = myfile.readline()

    a = a.split()

    for char in a:
        num = int(char, 2)
        print(num)

    #print(a)

    # for char in a:
    #     if char != " ":
    #         list.append(char)
    #     elif char == " ":
    #         for p in list:
    #             string += p
    #         print(string)
    #         list.clear()

    myfile.close()

main()



