def convertFromBinary():
    binaryNumber = input("Enter a binary number. ")
    number = 0
    length = len(binaryNumber)
    bits = 2**(length-1)
    binaryArray = [*binaryNumber]
   
    for i in range(length):
   
        if binaryArray[0] == "1":
            number += (1*bits)
            length -= 1
            bits = 2**(length - 1)
            del binaryArray[0]
       
        elif binaryArray[0] == "0":
            length -= 1
            bits = 2**(length - 1)
            del binaryArray[0]
       
        else:
            print("Not a one or zero.")
            length -= 1
            bits = 2**(length - 1)
            del binaryArray[0]
   
    print(number)
   
def convertFromDenary(binNum):
    binNum = bin(binNum).split("b")
    return binNum.pop()
    
while True:
    choice = input("Would you like to convert from or to binary? Enter to or from. ")

    if choice == "to":
        denary = int(input("Enter a number: "))
        binNum = denary
        print(f"The binary number for {denary} is {convertFromDenary(binNum)}")

    elif choice == "from":
        convertFromBinary()

    else:
        print("Not a valid input.")
        continue