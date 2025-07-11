import time
fibonacci = [1]

while True:
    if len(fibonacci) == 1:
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])
        print(f"{fibonacci}\n")
        time.sleep(1)