# This program will prove the Collatz conjecture!
import easygui

loopArray = {}
num = 1
x = num

while True:
    if len(loopArray) == 5:
        for i in range(len(loopArray)):
            loopArray.popitem()

    count = len(open('text.py').readlines())
    if count > 1:
        with open("text.py", "w") as f:
            f.write("")

    if num != 1:
        if num % 2 == 0:
            num: int = num / 2
        elif num % 2 == 1:
            num = num * 3
            num = num + 1
        elif isinstance(num, float):
            print(f"The number {num} is not in the loop.")
            easygui.msgbox(f"This number({num}) was not in the loop! We did it!", title="The conjecture is over!!!!!")
            break
    loopArray.update({x: "In the loop"})
    with open("text.py", "a+") as f:
        f.write(f"{str(loopArray)}\n")

    num += 1
    x += 1

print("Goodbye")