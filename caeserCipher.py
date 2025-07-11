import string, os

letters = list(string.ascii_lowercase)
noShift = letters.copy()

def decrypt(msg: list[str], shift) -> str:
    encryptedMsg = msg.copy()
    for i in range(shift):
        letters.append(letters.pop(0))
    decrypted = []
    for char in msg:
        if char not in letters:
            decrypted.append(char)
        else:
            charIndex = letters.index(char)
            decrypted.append(noShift[charIndex])

    return f"Encrypted message: {''.join(encryptedMsg)} | Original Message: {''.join(decrypted)}"

def encrypt(msg: list[str], shift) -> str:
    decryptedMsg = msg.copy()
    for i in range(shift):
        letters.append(letters.pop(0))
    encrypted = []
    for char in msg:
        if char not in letters:
            encrypted.append(char)
        else:
            charIndex = noShift.index(char)
            encrypted.append(letters[charIndex])

    return f"Original message: {''.join(decryptedMsg)} | Encrypted Message: {''.join(encrypted)}"

print(
"""
(1) Encrypt a Message
(2) Decrypt a Message
(Q) Exit Program
""")

while True:
    choice = input().lower()
    if choice == "1":
        print(encrypt(list(input("Message: ").lower()), int(input("Shift: "))))
    elif choice == "2":
        print(decrypt(list(input("Message: ").lower()), int(input("Shift: "))))
    elif choice == "q":
        break
    else:
        continue
    letters = noShift.copy()

print("Caesar Out!")
os.system("clear")