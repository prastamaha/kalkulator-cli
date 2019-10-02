# import function
import re

# header
print("")
print("==== Kalkulator Infinity =====")
print("ketik 'x' untuk keluar dari program" )

# default value for program
value = 0
run = True

def kalkulator():
 
    # deklarasikan value dan run sebagai global variabel
    global value
    global run

    # cek value awal
    if value == 0:
        print(0)
        inputUser = input(">> ")
    else:
        inputUser = input(value)

    # jika input user "x" maka akan keluar dari program
    if inputUser == "x":
        run = False
    else:
        inputUser = re.sub("[a-zA-Z.,:()" "[]","",inputUser)
        if value == 0:
            value = eval(inputUser)
        else:
            value = eval(str(value) + inputUser)

# function kalkulator akan di loop terus menerus
while run:
    kalkulator()